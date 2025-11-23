from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
import json
from django.http import JsonResponse



class viewMudarAvatar(LoginRequiredMixin,View):
    
    def post(self, request):
        print("chegou")
        data = json.loads(request.body)
        request.session["avatar"] = data.get("avatar")
        return JsonResponse({"status":"ok"})