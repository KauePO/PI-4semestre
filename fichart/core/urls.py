from django.urls import path
from .views.viewTelaLogin import viewTelaLogin
from .views.viewTelaCadastro import viewTelaCadastro
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', viewTelaLogin.as_view(), name="telaLogin"),
    path('cadastro/', viewTelaCadastro.as_view(), name="telaCadastro"),
]

urlpatterns += staticfiles_urlpatterns()
