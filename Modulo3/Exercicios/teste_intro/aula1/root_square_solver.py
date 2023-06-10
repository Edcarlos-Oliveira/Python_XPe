# Importado o modulo de raiz quadrada:
from math import sqrt

# Criando a função do teste (equação de 2º grau)
def rootSquareSolver(a, b, c):
    if b * b - 4 * a * c == 0:                              # Verifica se há apenas uma raiz
        r1 = (-b + sqrt(b * b - 4 * a * c)) / (2 * a)       # Calcula a primeira raiz
        return [r1]
    else:
        r1 = (-b + sqrt(b * b - 4 * a * c)) / (2 * a)       # Calcula a primeira raiz
        r2 = (-b - sqrt(b * b - 4 * a * c))/(2 * a)         # Calcula a segunda raiz
        return [r1, r2]                                     # Retorna uma 'array' com 2 posições


