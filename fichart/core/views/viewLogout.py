from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout

class viewLogout(LoginRequiredMixin, View):
    
    def get(self, request):
        logout(request)
        return render(request, "templateLogin.html")