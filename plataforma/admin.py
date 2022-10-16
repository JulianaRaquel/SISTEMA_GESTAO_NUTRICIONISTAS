from django.contrib import admin
from .models import Paciente, DadosPaciente, NovaRefeicao, Opcao

admin.site.register(Paciente)
admin.site.register(DadosPaciente)
admin.site.register(NovaRefeicao)
admin.site.register(Opcao)
