import unittest
from root_square_solver import rootSquareSolver # Modulo criado no arquivo

# Criando a classe e a função dos testes:
class CheckRootSquareSolver(unittest.TestCase):
    # Checando se há 2 raizes:
    def test_checkTwoRoots(self):               # Quando se trata de um teste, precisa manter o 'test_' antes do que vai ser verificado
        response = rootSquareSolver(1, -5, 6)   # Para calcular uma raiz de segundo grau (a, b, c)
        self.assertEqual(len(response), 2)      # Checa se tem duas raízes (assrtEqual => Mostra que uma coisa é igual a outra), nesse caso se há 2 raízes

    # Checando se há os valores declarados:
    def test_checkTwoRootValue1(self):
        response = rootSquareSolver(1, -5, 6)
        self.assertIn(response[0], [2, 3])      # Varifica se na posição '0' do 'array' tem o 2 ou 3 

    def test_checkTwoRootValue2(self):
        response = rootSquareSolver(1, -5, 6)
        self.assertIn(response[1], [2, 3])      # Verifica se na posição '1' do 'array' tem o 2 ou 3

    # Verificando se há apenas uma raiz:
    def test_checkOneRoots(self):
        response = rootSquareSolver(1, -4, 4)
        self.assertEqual(len(response), 1)
        

