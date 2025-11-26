from django.urls import path


from .views.viewTelaLogin import viewTelaLogin
from .views.viewTelaCadastro import viewTelaCadastro
from .views.viewTelaCadastro import viewTelaCadastro
from .views.viewTelaEscolhaRaca import viewTelaEscolhaRaca
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views.viewTelaClasses import viewTelaClasses
from .views.viewTelaMagia import viewTelaMagia
from .views.viewTelaAntecedente import viewTelaAntecedente
from .views.viewFichaPersonagem import viewFichaPersonagem
from .views.viewTelaAtributos import viewTelaAtributos
from .views.viewPaginaInicial import viewPaginaInicial
from .views.viewLogout import viewLogout
from .views.viewAssinarPlano import viewAssinarPlano
from .views.viewSucessoPagamento import viewSucessoPagamento
from .views.viewTelaEscolhaEquipamentos import viewTelaEquipamentos
from .views.viewMudarAvatar import viewMudarAvatar

from .views.viewVisualizarFicha import viewVisualizarFicha

urlpatterns = [
    path('', viewTelaLogin.as_view(), name="telaLogin"),
    path('cadastro/', viewTelaCadastro.as_view(), name="telaCadastro"),
    path('selecaoRaca/',viewTelaEscolhaRaca.as_view(), name="TelaEscolhaRaca"),
    path('selecaoClasse/',viewTelaClasses.as_view(), name="TelaClasses"),
    path("selecaoMagia/",viewTelaMagia.as_view(), name="TelaMagia"),
    path('selecaoAntecedente/',viewTelaAntecedente.as_view(), name="TelaAntecedente"),
    path('fichaPersonagem/', viewFichaPersonagem.as_view(), name="fichaPersonagem"),
    path('visualizarFicha/<int:idPersonagem>/', viewVisualizarFicha.as_view(), name="visualizarFicha"),
    path('selecaoAtributos/',viewTelaAtributos.as_view(), name='TelaAtributos'),
    path("paginaInicial/", viewPaginaInicial.as_view(), name="paginaInicial"),
    path("logout/",viewLogout.as_view(), name="logout"),
    path("assinarPlano/", viewAssinarPlano.as_view(), name="assinarPlano"),
    path("sucessoPagamento/", viewSucessoPagamento.as_view(), name="sucessoPagamento"),
    path("selecaoEquipamento/", viewTelaEquipamentos.as_view(), name="TelaEquipamento"),
    path("mudarAvatar/", viewMudarAvatar.as_view(), name="mudarAvatar")
]
