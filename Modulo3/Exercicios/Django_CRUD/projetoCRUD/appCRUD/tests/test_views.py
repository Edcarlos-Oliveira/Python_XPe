# Importando os modulos necessários:
from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy
from appCRUD.models import User

# Criando a classe para os testes:
class ViewTest(TestCase):
    def setUp(self):
        self.dados = {
            'nome': 'Nome',
            'telefone': 329999,
            'email': 'Email'
        }
        self.client = Client()

    # Testando o 'index', retorna código (200):
    def test_index(self):
        request = self.client.get(reverse_lazy('index'))
        self.assertEquals(request.status_code, 200)
        
    # Testando o 'criar', retorna o código (302):
    def test_criar(self):
        request = self.client.post(reverse_lazy('criar'), data=self.dados)
        self.assertEquals(request.status_code, 302)
