from django.urls import path
from .views.viewTelaLogin import viewTelaLogin
from .views.viewTelaClasses import viewTelaClasses

urlpatterns = [
    path('', viewTelaLogin.as_view(), name="telalogin"),
    path('criacao/classes/', viewTelaClasses.as_view(), name="telacriacaoclasse"),
]