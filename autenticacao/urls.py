from django.urls import path
from .views import cadastro, logar, sair, ativar_conta


urlpatterns = [
    path('cadastro/', cadastro, name='cadastro'),
    path('logar/', logar, name='logar'),
    path('sair/', sair, name='sair'),
    path('ativar_conta/<str:token>/', ativar_conta, name="ativar_conta")
]