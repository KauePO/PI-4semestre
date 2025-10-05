from django.urls import path
from .views.viewTelaLogin import viewTelaLogin
from .views.viewTelaCadastro import viewTelaCadastro
from .views.viewTelaCadastro import viewTelaCadastro
from .views.viewTelaEscolhaRaca import viewTelaEscolhaRaca
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views.viewTelaClasses import viewTelaClasses

urlpatterns = [
    path('', viewTelaLogin.as_view(), name="telaLogin"),
    path('cadastro/', viewTelaCadastro.as_view(), name="telaCadastro"),
    path('selecaoClasse/',viewTelaEscolhaRaca.as_view(), name="TelaEscolhaRaca")
]
