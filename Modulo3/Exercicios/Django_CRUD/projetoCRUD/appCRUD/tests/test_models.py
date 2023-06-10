# Importando modulos necessários:   
from django.test import TestCase
from appCRUD.models import User

class StrTest(TestCase):
    def setUp(self):
        self.user = User(nome='Edcarlos', telefone=23232, email='aaaaa@eeee.com.br')

    def test_str(self):
        self.assertEquals(str(self.user), 'Nome: Edcarlos, Telefone: 23232, Email: aaaaa@eeee.com.br')
