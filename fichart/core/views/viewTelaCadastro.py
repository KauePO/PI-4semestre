from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


class viewTelaCadastro(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("TelaClasses")
            
        return render(request, "templateCadastro.html")

    def post(self, request):
        print(request.POST['username'])
        form = UserCreationForm(request.POST)

        if not form.is_valid():
            error = list(form.errors.values())[0]
            print(error)
            return render(request, "templateCadastro.html",{"error":error})

        form.save()
        
        return redirect('telaLogin')

        
