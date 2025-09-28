from django.views import View
from django.http import HttpResponse

class viewTelaLogin(View):
    def get(self, request):
        html = '<html lang="en"><body>It is now.</body></html>' 
        return HttpResponse(html)
