from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login

class viewTelaLogin(View):
    def get(self, request):

        if request.user.is_authenticated:
            return redirect("TelaEscolhaRaca")
            
        return render(request, "templateLogin.html")

    def post(self,request):

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        
        if user is None:
            print('Esse usuário não existe')
            return redirect('telaLogin')

        
        login(request,user)
        return redirect('TelaEscolhaRaca')
