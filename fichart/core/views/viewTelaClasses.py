from django.views import View
from django.shortcuts import render

class viewTelaClasses(View):
    def get(self, request):
        classes = [
        {
            'id': 1,
            'name': 'Guerreiro',
            'icon': '\static\frieren2II.png',
            'description': 'Um combatente robusto que dddd armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaam combatente robusto que dddd armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaam combatente robusto que dddd armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaam combatente robusto que dddd armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaam combatente robusto que dddd armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaam combatente robusto que dddd armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaam combatente robusto que dddd armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaam combatente robusto que dddd armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...Um combatente robusto que uaaaaaaaaaaaa armas poderosas...',
        },
        {
            'id': 2,
            'name': 'Ladino',
            'icon': '\static\frieren2II.png',
            'description': 'Um combatente robusto que uaaaaaaaaaaaa armas poderosas...',
        },
        {
            'id': 3,
            'name': 'Guerreiro',
            'icon': '\static\frieren2II.png',
            'description': 'Um combatente robusto que uaaaaaaaaaaaa armas poderosas...',
        },
        {
            'id': 4,
            'name': 'Guerreiro',
            'icon': '\static\frieren2II.png',
            'description': 'Um combatente robusto que uaaaaaaaaaaaa armas poderosas...',
        },
        {
            'id': 51,
            'name': 'Guerreiro',
            'icon': '\static\frieren2II.png',
            'description': 'Um combatente robusto que uaaaaaaaaaaaa armas poderosas...',
        },
        {
            'id': 15,
            'name': 'Guerreiro',
            'icon': '\static\frieren2II.png',
            'description': 'Um combatente robusto que uaaaaaaaaaaaa armas poderosas...',
        },
        {
            'id': 61,
            'name': 'Guerreiro',
            'icon': '\static\frieren2II.png',
            'description': 'Um combatente robusto que uaaaaaaaaaaaa armas poderosas...',
        },
        {
            'id': 12,
            'name': 'Guerreiro',
            'icon': '\static\frieren2II.png',
            'description': 'Um combatente robusto que uaaaaaaaaaaaa armas poderosas...',
        },
        {
            'id': 122,
            'name': 'Guerreiro',
            'icon': '\static\frieren2II.png',
            'description': 'Um combatente robusto que uaaaaaaaaaaaa armas poderosas...',
        },
        {
            'id': 13,
            'name': 'Guerreiro',
            'icon': '\static\frieren2II.png',
            'description': 'Um combatente robusto que uaaaaaaaaaaaa armas poderosas...',
        },
        {
            'id': 133,
            'name': 'Guerreiro',
            'icon': '\static\frieren2II.png',
            'description': 'Um combatente robusto que uaaaaaaaaaaaa armas poderosas...',
        },
        {
            'id': 1333,
            'name': 'Guerreiro',
            'icon': '\static\frieren2II.png',
            'description': 'Um combatente robusto que uaaaaaaaaaaaa armas poderosas...',
        },
        
    ]
        return render(request, 'templateTelaClasses.html', {'classes': classes})