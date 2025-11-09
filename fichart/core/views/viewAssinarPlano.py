from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import redirect
from core.models import Usuario
import requests

class viewAssinarPlano(LoginRequiredMixin, View):
    def get(self, request):
        
        user = Usuario.objects.get(user = request.user)
        
        
        url = "https://api.abacatepay.com/v1/billing/create"
        token = "abc_dev_RJh2nXJLpFtyKGRt0BDNBxAk"
        headers ={
            "Authorization":f"Bearer {token}",
            "Content-Type":"application/json"
        }
        
        data = {
            "frequency": "ONE_TIME",
            "methods": ["PIX"],
            "products": [
                {
                    "externalId": "1",
                    "name": "Assinatura Aventureiro",
                    "description": "Acesso a 50 fichas.",
                    "quantity": 1,
                    "price": 1399
                }
            ],
            "returnUrl": "http://localhost:8000/paginaInicial/",
            "completionUrl": "http://localhost:8000/sucessoPagamento/",
            "customer": {
                "name": request.user.username,
                "cellphone": "(11) 4002-8922",
                "email": "daniel_lima@abacatepay.com",
                "taxId": "51911125800"
            },
        }
        
        response = requests.post(url, headers=headers, json=data)
        responseData = response.json()
        urlPagamento = responseData.get("data",{}).get("url")
        
        return redirect(urlPagamento)
        
    