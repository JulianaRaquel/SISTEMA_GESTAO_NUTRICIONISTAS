from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Paciente, DadosPaciente, NovaRefeicao, Opcao, Refeicao
from django.contrib import messages
from django.contrib.messages import constants
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt

@login_required(login_url='/logar/')
def pacientes(request):
    if request.method == "GET":
        pacientes = Paciente.objects.filter(nutri=request.user)
        return render(request, 'pacientes.html', {'pacientes': pacientes})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        sexo = request.POST.get('sexo')
        idade = request.POST.get('idade')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')

        if (len(nome.strip()) == 0) or (len(sexo.strip()) == 0) or (len(idade.strip()) == 0) or (
                len(email.strip()) == 0) or (len(telefone.strip()) == 0):
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect('/pacientes/')

        if not idade.isnumeric():
            messages.add_message(request, constants.ERROR, 'Digite uma idade válida')
            return redirect('/pacientes/')

        paciente = Paciente.objects.filter(email=email)

        if paciente.exists():
            messages.add_message(request, constants.ERROR, 'Já existe um paciente com esse E-mail')
            return redirect('/pacientes/')

        try:
            paciente = Paciente(nome=nome,
                                 sexo=sexo,
                                 idade=idade,
                                 email=email,
                                 telefone=telefone,
                                 nutri=request.user)

            paciente.save()

            messages.add_message(request, constants.SUCCESS, 'Paciênte cadastrado com sucesso')
            return redirect('/pacientes/')
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('/pacientes/')


@login_required(login_url='/logar/')
def dados_paciente_listar(request):
    if request.method == "GET":
        pacientes = Paciente.objects.filter(nutri=request.user)
        return render(request, 'dados_paciente_listar.html', {'pacientes': pacientes})

@login_required(login_url='/logar/')
def dados_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    if paciente.nutri != request.user:
        messages.add_message(request, constants.ERROR, 'Esse paciente não é seu')
        return redirect('/dados_paciente/')
    if request.method == "GET":
        dados = DadosPaciente.objects.filter(paciente=paciente)
        return render(request, 'dados_paciente.html', {'paciente': paciente, 'dados': dados})
    elif request.method == "POST":
        peso = request.POST.get('peso')
        altura = request.POST.get('altura')
        gordura = request.POST.get('gordura')
        musculo = request.POST.get('musculo')

        hdl = request.POST.get('hdl')
        ldl = request.POST.get('ldl')
        ctotal = request.POST.get('ctotal')
        triglicerideos = request.POST.get('trigliceridios')

        paciente = DadosPaciente(paciente=paciente, data=datetime.now(), peso=peso, altura=altura,
                                 percentual_gordura=gordura, percentual_musculo=musculo, colesterol_hdl=hdl,
                                 colesterol_ldl=ldl, colesterol_total=ctotal, triglicerideos=triglicerideos)

        paciente.save()
        messages.add_message(request, constants.SUCCESS, 'Dados cadastrados com sucesso')
        return redirect('/dados_paciente_listar/')


@login_required(login_url='/logar/')
@csrf_exempt
def grafico_peso(request, id):
    paciente = Paciente.objects.get(id=id)
    dados = DadosPaciente.objects.filter(paciente=paciente).order_by("data")

    pesos = [dado.peso for dado in dados]
    labels = list(range(len(pesos)))
    data = {'peso': pesos,
            'labels': labels}
    return JsonResponse(data)

@login_required(login_url='/logar/')
def plano_alimentar_listar(request):
    if request.method == "GET":
        pacientes = Paciente.objects.filter(nutri=request.user)
        return render(request, 'plano_alimentar_listar.html', {'pacientes': pacientes})

@login_required(login_url='/logar/')
def plano_alimentar(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    if paciente.nutri != request.user:
        messages.add_message(request, constants.ERROR, 'Esse paciente não é seu')
        return redirect('/dados_paciente/')

    elif request.method == "GET":
        refeicoes = NovaRefeicao.objects.filter(paciente=paciente).order_by("horario")
        return render(request, 'plano_alimentar.html', {'paciente': paciente, 'refeicoes': refeicoes})


@login_required(login_url='/logar/')
def refeicao(request, id_paciente):
    paciente = get_object_or_404(Paciente, id=id_paciente)
    if paciente.nutri != request.user:
        messages.add_message(request, constants.ERROR, 'Esse paciente não é seu')
        return redirect('/dados_paciente/')
    elif request.method == "POST":
        titulo = request.POST.get('titulo')
        horario = request.POST.get('horario')
        carboidratos = request.POST.get('carboidratos')
        proteinas = request.POST.get('proteinas')
        gorduras = request.POST.get('gorduras')

        r1 = NovaRefeicao(paciente=paciente, titulo=titulo, horario=horario, carboidratos=carboidratos,
                          proteinas=proteinas, gorduras=gorduras)
        r1.save()

        messages.add_message(request, constants.SUCCESS, 'Refeição cadastrada')
        return redirect(f'/plano_alimentar/{id_paciente}')

def opcao(request, id_paciente):
    if request.method == "POST":
        id_refeicao = request.POST.get('refeicao')
        imagem = request.FILES.get('imagem')
        descricao = request.POST.get('descricao')

        opcao = Opcao(refeicao_id=id_refeicao,
                      imagem=imagem,
                      descricao=descricao)
        opcao.save()

        messages.add_message(request, constants.SUCCESS, 'Refeição cadastrada')
        return redirect(f'/plano_alimentar/{id_paciente}')

