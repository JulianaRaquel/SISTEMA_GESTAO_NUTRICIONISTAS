from django.contrib import admin
from .models import Paciente, DadosPaciente, NovaRefeicao, Opcao, Refeicao

admin.site.register(Paciente)
admin.site.register(DadosPaciente)
admin.site.register(NovaRefeicao)
admin.site.register(Opcao)
admin.site.register(Refeicao)
