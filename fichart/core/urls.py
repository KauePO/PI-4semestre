from django.urls import path
from .views.viewTelaLogin import viewTelaLogin
from .views.viewTelaCadastro import viewTelaCadastro
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views.viewTelaClasses import viewTelaClasses

urlpatterns = [
    path('', viewTelaLogin.as_view(), name="telaLogin"),
    path('cadastro/', viewTelaCadastro.as_view(), name="telaCadastro"),
    path('criacao/classes/', viewTelaClasses.as_view(), name="telacriacaoclasse"),
]

urlpatterns += staticfiles_urlpatterns()
