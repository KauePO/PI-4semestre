from django.test import TestCase
from core.models import Usuario, User

class testSignals(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user("jonh","jonh@teste.com","1234")
        self.user.save()
        
    def test_signal_post_save_user(self):
        usuario = Usuario.objects.get(user = self.user)
        
        self.assertTrue(usuario)