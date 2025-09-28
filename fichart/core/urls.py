from django.urls import path
from .views.viewTelaLogin import viewTelaLogin

urlpatterns = [
    path('', viewTelaLogin.as_view(), name="telalogin"),
]