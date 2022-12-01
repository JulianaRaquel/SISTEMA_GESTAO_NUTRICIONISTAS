from django.db import models
from django.contrib.auth.models import User

class Paciente(models.Model):
    choices_sexo = (('F', 'Feminino'),('M', 'Masculino'))
    nome = models.CharField(max_length=50)
    sexo = models.CharField(max_length=1, choices=choices_sexo)
    idade = models.IntegerField()
    email = models.EmailField(default='blank')
    telefone = models.CharField(max_length=19)
    nutri = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class DadosPaciente(models.Model):
    # Se o paciente for excluido, todos os dados também serão excluídos
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    # data em  que os dados foram coletados pelo nutricionista
    data = models.DateTimeField()
    peso = models.IntegerField()
    altura = models.IntegerField()
    percentual_gordura = models.IntegerField()
    percentual_musculo = models.IntegerField()
    colesterol_hdl = models.IntegerField()
    colesterol_ldl = models.IntegerField()
    colesterol_total = models.IntegerField()
    triglicerideos = models.IntegerField()

    def __str__(self):
        return f"Paciente({self.paciente.nome}, {self.peso})"


class Refeicao(models.Model):
    refeicao = models.CharField(max_length=20)

    def __str__(self):
        return self.refeicao

class NovaRefeicao(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=30)
    horario = models.TimeField()
    carboidratos = models.IntegerField()
    proteinas = models.IntegerField()
    gorduras = models.IntegerField()

    def __str__(self):
        return str(self.titulo)

class Opcao(models.Model):
    refeicao = models.ForeignKey(NovaRefeicao, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='opcoes')
    descricao = models.TextField()

    def __str__(self):
        return self.descricao

