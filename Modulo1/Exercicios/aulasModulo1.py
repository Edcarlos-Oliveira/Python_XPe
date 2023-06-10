# -*- coding: utf-8 -*-
"""aulasModulo1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ieo3AInuDpIQuuRbwYptIV5Fvi10fqbR
"""

nome = 'Edcarlos Oliveira'
print('Olá', nome, 'seja bem vindo!')

numero = 1
print(numero + 2)

# Criando Variáveis:

pessoa = 'Edcarlos Oliveira'
idade = 47
altura = 1.80

print(f'Olá {pessoa}, você tem {idade} anos e tem {altura:.2f} de altura')

# Analisando erros:
''' Principais erros: 
    Erros de Sintaxe => Constatado antes da execução do código.
    Erros em Tempo de Execução => Executa e depois verifica os trechos errados
    Erros Lógicos => Mais difícil a constatação
'''
# Erro de Sintaxe:
x = 3
y = 5
print x + y # Falta os parenteses

# Erro em Tempo de execução:
a = 1000
print(a)
b = 0
print(b)
c = a/b
print(c) # Aqui está o erro.

# Erros Lógicos:
x = 5.0
y = 7.0
z = 12.0
media = x+y+z/3 # Nesse caso haverá erro no resultado pela ordem de precedência.
media2 = (x+y+z)/3 # Assim seria o correto
print(media)
print(media2)

# Trabalhando com tipo int:

x = 5
y = -3
big = 12354558896677588655478869665545
print(x + y)

# Trabalhando com float:
a = 3.5
b = 2.1
print(a + b)

# Trabalhando com bool
h = ''
i = False
if h == True:
  h = 'Parabéns você é habilitado!'
  print(h)
else:
  print(f'Você não é habilitado {i}')

# Trabalhando com str:
nome = 'edcarlos oliveira'
print(nome)
type(nome)

print(nome[0]) # Mostra o 'E'
print(nome[-17]) # Mostra o 'E'
print(nome[2:8]) # Mostra 'carlos'
print(len(nome)) # Conta os itens
print(nome.upper()) # Maiusculas
print(nome.lower()) # Minusculas
print(nome.title()) # As primeiras letras em maiusculas
print(nome.replace('oliveira', 'lima')) # Faz a substituição, nesse caso o 'oliveira' por 'lima'
print(nome.startswith('oliveira')) # Verifica se o nome começa com 'oliveira' retorna valor lógico 'true ou false'
print(nome.endswith('oliveira')) # verifica se termina com 'oliveira'
print(nome.find('edcarlos')) # retorna o indice da primeira ocorrencia da palavra 'edcarlos', nesse caso '0'
print(nome.split()) # Separa os itens entre virgulas com [] lista.

# Trabalhando com NoneType(ideal para ver o tipo de determinado codigo):
b = 10
type(b)

a = 6.5
type(a)

c = 'valor'
type(c)

# Conversão dos tipos de DADOS:
an = 1976
aa = 2023
i = aa - an
print(f'Sua idade é {i:.1f} anos.') # Mais moderno, definido o float com ':.1f'.
print('Sua idade é ' + str(i) + ' anos.') # Poderia ser reescrito assim.
print(float(i))
print(bool(i)) # Só se a idade fosse '0' retornaria 'false'
print(bool(0))
print(float(True)) # Será sempre 1.0
print(float(False)) # Será sempre 0.0
print(bool('palavra')) # Será sempre 'True'
print(bool('')) # Será sempre 'Falsa'
print(str(None)) # Não consegue converter para int ou float, só esses dois casos
print(bool(None)) # Sempre será 'False'

# Fluxos de Controles (Condicionais):

idade = 15
if idade >= 18 and idade < 60:
  print(f'Você com {idade} anos é maior de idade.')
elif idade >= 60:
  print(f'Você com {idade} anos é idoso.')
else:
  print(f'Você com {idade} está entre criança e adolescente')

# Fluxos de Controles (Repetição):

a = 15
soma = 0


while a >= 0:
  soma += a
  a -= 1
print(f'A soma dos primeiros inteiros é {soma}.')

num = '4589'
soma = 0

for i in num:
  #print(i)
  soma += int(i) # Transformou a str em int
print(f'A soma é {soma}')

pal = 'Araraquara'.upper()
cont = 0

for letra in pal:
  if letra == 'A':
    cont += 1
print(f'A letra "a" aparece {cont} vez(s) na palavra {pal}.')

for n in range(250, 301):
  if n % 21 == 0:
    print(f'O número encontrado foi {n}')
    break # Usando o 'break' exibe apenas o primeiro numero encontrado.

# Estruturas de Dados:
'''
   Listas [list] => Ordenada e Mutável
   Tupla (tuple) => Ordenada e Imutável
   Conjunto {set} => Não ordenada, mutável e valores únicos
   Dicionário {dict} => Mapeamento(key, value), não ordenado e mutável
''' 

# Trabalhando com listas: 
l1 = [1,2,3,4]
l2 = [4,3,2,1]
print(l1)
print(l2)

# Lista com valores heterogeneos:
het = [2, 'a', 5.44, True]
print(het)

# Verificando Idades em Listas [list]:

idades = [27,48,1,25,32,52,75,10,36,8,9]

maior = idades[0]
menor = idades[0]
for idade in idades:
  if idade > maior:
    maior = idade
  if idade < menor:
    menor = idade
print(maior)
print(menor)
print(idades)
print(max(idades))
print(min(idades))
print(sum(idades))  # Soma todos os valores da lista

# Trabalhando com Tuplas (tuple):

tp = (0, 1, 2, 3, 4) # Aceita todas as alterações aplicadas em lista, exceto alteração dos dados.
print(tp)

# Trabalhando com Conjuntos {set}:

c1 = {3,0,1,4,3}
print(c1)

c2 = {1,4,3,0,2}
print(c2)

A = {1,2,3,4,5}
B = {4,5,6,7,8}
print('A = ', A)
print('B = ', B)

# UInião dos conjuntos (A | B):
print('A | B => ', A | B) # junta os dois conjuntos
print('A.union(B) =>', A.union(B)) # Também junta os conjuntos

# Interseção dos conjuntos (A & B):
print('A & B =>', A & B)
print('A.intersection(B) => ', A.intersection(B)) # Existe nos dois conjuntos

# difrença dos Conjuntos (A - B) e (B - A):
print('A - B =>', A - B) # Os números que existem só em A
print('A.difference(B) =>', A.difference(B))
print('B - A => ', B - A)
print('B.difference(A) => ', B.difference(A))

# Criação de novos Conjuntos:

c1 = {1,2,3,4,5}
c2 = {4,5}
c3 = {91,92,93}

# Adiciona um elemento:
c1.add(6) # Adiciona o '6' no conjunto 'c1'
print(c1)
c2.update({2,4,6,8}) # Adiciona os itens declarados desconsiderando os repetidos
print(c2)

# Descartando elementos dos conjuntos:
c1.remove(3) # Caso não exista o numero a ser removido, retorna um erro
print('Removido o 3 do conjunto: ', c1)

c1.discard(2) # Nesse caso não retorna erro caso o item não exista
print('Removendo o 2 com discard: ', c1)

# Verifica se os elementos são em comum:
print(c1.isdisjoint(c2)) # Retorna False pq tem itens em comum.
print(c2.isdisjoint(c3)) # Retorna True pq não tem nenhum item em comum.

# Verifica se o conjunto é subconjunto de outro:
print(c1)
print(c2)
print(c1.issubset(c2)) # Se é subconjunto de c2
print(c2.issubset(c1)) # Se c2 é subconjunto de c1

# Verifica se um contem o outro:
print(c1)
print(c2)
print(c1.issuperset(c2)) # Se c1 contem c2
print(c2.issuperset(c1)) # Se c2 contem c1

# Resolvendo Problemas com Conjuntos:

ING = {'Gabriel', 'Caio', 'Maria', 'Juliano', 'Flávia', 'Rubens', 'Bruna'}
ESP = {'Caio', 'Artur', 'Beatriz', 'Carolina', 'Maria', 'Juliano', 'Bruna', 'Rui'}
FRA = {'Pedro', 'Bruna', 'Paula', 'Maria', 'Flávia', 'Rui', 'Carolina'}

# Unindo todos os conjuntos:
todos = ING | ESP | FRA

# Exibindo o resultado:
print(todos) # Nesse caso por ser conjunto não haverá repetição

# Criando a interseção para identificar os repetidos:
print(f'Turmas de Ingles e Espanhol {ING & ESP}')
print(f'Turmas de Ingles e Francês {ING & FRA}')
print(f'Turmas de Espanhol e Francês {ESP & FRA}')

# Criando o conjunto dos alunos com descontos:
# Critério estar matriculado em mais de 2 cursos
alu_desc = (ING & ESP | (ING & FRA) | (ESP & FRA)) # Junta os conjuntos e não repete os itens
print(f'Relação dos Alunos com descontos: {alu_desc}')

# Trabalhando com dicionários {dict}

d1 = {'nome': 'Edcarlos', 'idade': 46, 'sexo': 'M' }
print(d1['nome'])

# Adicionando novo item:

d1['endereco'] = 'Rua 123'
print(d1)

from re import L
# Trabalhando com Funções:

l1 = [1,2,3,4,5]
l2 = [3,1,5,9,0,8,2,3,4]
l3 = [12,43,23,12,789]

soma_l1 = 0
for item in l1:
  soma_l1 += item

soma_l2 = 0
for item in l2:
  soma_l2 += item

soma_l3 = 0
for item in l3:
  soma_l3 += item

print()
print(f'Soma de l1 = {soma_l1}')
print(f'Soma de l2 = {soma_l2}')
print(f'Soma de l3 = {soma_l3}')

# Transformando o code anterior em função:
def soma_lista(lista):
  soma = 0
  for item in lista:
    soma += item
  return soma

soma_l1 = soma_lista(l1)
soma_l2 = soma_lista(l2)
soma_l3 = soma_lista(l3)

print('Usando a soma com função:')
print(f'Soma de l1 = {soma_l1}')
print(f'Soma de l2 = {soma_l2}')
print(f'Soma de l3 = {soma_l3}')

print('Multiplicando as listas com funções:')
def multi_lista(lista):
  res = 1 # Sempre 1 qundo se trata de multiplicação.
  for item in lista:
    res *= item
  return res

print(multi_lista(l1))
print(multi_lista(l2))
print(multi_lista(l3))

print('Definindo mais funções:')

def saudacao (nome):
  print(f'Olá {nome}. Seja bem-vindo(a)!')
  return ''

def a_quad (lado):
  return lado * lado

def a_tri (b, alt):
  return (b * alt)/2

# Definição do que vai para os parâmetros em cada função:

print(saudacao('Edcarlos'))
print(a_quad(8))
print(a_tri(5,2))

print('Outros exemplos de funções:')

def div(dividendo, divisor):
  if divisor == 0:
    print('ERROR! Divisor igual a zero!')
    return 'Escolha um divisor maior que zero' # Funciona como 'break'
  return dividendo / divisor

print(div(10,4))

print('Quociente e resto')

def div_qr(dividendo, divisor):
  if divisor == 0:
    print('ERROR! Divisor igual a zero')
    return''
  quociente = dividendo // divisor
  resto = dividendo % divisor
  return (quociente, resto)

print(div_qr(10,4))

print()

# Poderia ser reescrita assim:

def div_invalido(divisor):
  if divisor == 0:
    print('ERROR! Divisor inválido(igual a zero)')
    return True
  return False

def div(dividendo, divisor):
  if (div_invalido(divisor)):
    return 'failed'
  return dividendo / divisor

print('Quociente e resto')

def div_qr(dividendo, divisor):
  if (div_invalido(divisor)):
    return 'failed'
  quociente = dividendo // divisor
  resto = dividendo % divisor
  return (quociente, resto)

print(div(10,0))
print(div_qr(10,0))

# Trabalhando com Modulos:

# Define valor de PI:

pi = 3.141592

# Calcula a área do quadrado:
def quad (l):
  return l ** 2

# Calcula a área de um triângulo:
def tri (b, h):
  return (b * h)/2

# Calcula a área de um círculo:
def circ (r):
  return pi * (r ** 2)

# Calcula a área do elipse:
def elip (a, b):
  return pi * a * b

# Calcula a área do trapézio:
def trap (B, b, h):
  return (B + b) * h / 2

# Importando o Modulo criado (areas.py)
import areas # Nesse caso importa tudo que está na função área

print(areas.tri(5,8))

print(areas.pi)

# Importando uma função especifica de (areas.py)
from areas import tri # Nesse caso importou só a função do triângulo.

print(tri(5,6)) # nesse caso basta declarar só o 'tri'

# Modulos Nativos do Python:

import math # Funções matemáticas

print(math.cos(100)) # Calcula o cosceno de 100.
print(math.log(10)) # Calcula o logaritmo de 10.

import itertools # Cria sequências elaboradas

# Combinação de 3 em 3 da sequência declarada:
print(list(itertools.combinations('ABCD', 3)))

# Permutação de 2 em 2:
print(list(itertools.permutations(['a', 'b', 'c'], 2)))

from datetime import datetime, timedelta # Importando diretamente a função:

# Trabalhado com data e horas:
print(datetime.now()) # Nesse caso mostra o horário do servidor local ou máquina que está sendo usada.

# Mostrando datas futuras:
print(datetime.now() + timedelta(days=7)) # Nesse caso a data daqui a 7 dias.

import random # Cria números aleatórios:
print('Aleatório entre 0 e 1: ', random.random()) # Retorna numeros float
print('Aleatorio entre 50 e 100: ', random.randint(50,100) ) # Retorna Inteiro

import os # Para criar interações com o sistema operacional:

# Interações com o sistema operacional:
os.mkdir('Pasta') # cria um diretório chamado pasta

# Instalando Pacotes externos Pypi:

# Instalado pacotes pelo '!pip':

!pip install colorama # Instala um pacote de cores e estilos:

# Trabalhando com cores do pacote 'colorama':
from colorama import Fore, Back, Style
print('Texto Normal') 
print(Fore.BLUE + 'Texto em Azul') 
print(Back.BLUE + Fore.WHITE + 'Texto em branco com fundo azul')
print(Style.RESET_ALL + 'Texto Normal Novamente') # apaga todas as configurações anteriores.

# Manipulando arquivos em disco:
''' r => Somente Leitura
    w => Modo escrita, cria um arquivo, caso ainda não exista, ou substitui o atual.
    x => Modo escrita, cria um arquivo, se o arquivo existir, retorna erro. 
    a => Modo escrita, cria um arquivo, caso ainda não exista, adciona dados no final.
    t => Abre o arquivo no modo texto
    b => Abre o arquivo no modo binário.
'''

# Abrindo o arquivo :
arquivo = open('arq_leitura.txt', 'r')
arquivo.close() # Fecha o arquivo

# Abrindo arquivo modo escrita 'w':
arquiv = open('valores.txt', 'w')
arquiv.close()

# Abrindo e criando arquivo no modo 'x'
arquivo = open('valores_2.txt', 'x')
arquivo.close()

arquivo = open('valores.txt', 'at')
arquivo.close()

# Lendo todo conteúdo de uma só vez:
arquivo = open('cidades.txt', 'r')
linhas = arquivo.read()
arquivo.close()
print(linhas)

# Lendo arquivo criando listas de strings:
arquivo = open('cidades.txt', 'r')
linhas = arquivo.readlines() # lendo em linhas
arquivo.close()
print(linhas)

# Novas linhas usando o 'for', nesse exemplo retirou o '\n' da execução anterior:
novas_linhas = list()
for l in linhas:
  novas_linhas.append(l.rstrip())
print(novas_linhas)

# Transformando string em inteiro e somando os numeros da população:
arquivo = open('cidades.txt', 'r')
soma = 0
for linha in arquivo:
  cidade = linha.split(' ') # coloca os espaços
  populacao = int(cidade[-1]) # transforma str em int
  print(populacao)
  soma += populacao
arquivo.close()
print(f'Total das popoluações {soma}')

# Escrevendo nos arquivos:
arquivo = open('cidades.txt', 'a')
arquivo.write('Bahia; 3500\n') # adiciona no arquivo texto a str
arquivo.close()

# Escrevendo mais de um arquivo:
linhas = ['Maceio; 2500\n',
          'Santa Catarina; 2000\n',
          'Mato Grosso; 1500\n',
          'Acre; 2000\n'
]
arquivo = open('cidades.txt', 'a')
arquivo.writelines(linhas) # Adiciona várias linhas
arquivo.close()

# Recursos Úteis da Linguagem:

# Sintaxe Normal do code:
pot = list()
for n in range(1,11):
  pot.append(n ** 2)
print(pot)

# Refazendo o code utilizando a Compreensão de Listas (list Comprehension):
pot = [n ** 2 for n in range(1,11)] # Nesse caso não precisa do 'append' pois a lógica está dentro da própria lista.
print(pot)

# Multiplique por 10 os números de 1 a 15 SINTAXE NORMAL:
num = list()
m = 1
for n in range(1,16):
  num.append(n * 10)
  m *= n
print(num)

# Refazendo o code utilizando a Compreensão de Listas (list Comprehension):
num = [n * 10 for n in range(1,16)]
print(num)

# Verificando se é Par ou Impar SINTAXE NORMAL:
num = list()
for n in range(0,10):
  if n % 2 == 0:
    num.append(True)
  else:
    num.append(False)
print(num)

# Refazendo o code utilizando a Compreensão de Listas (list Comprehension):
num = [n % 2 == 0 for n in range(0,10)]
print(num)

# Criando uma lista com os números impares de 1 a 10 elevados a 2 SINTAXE NORMAL:
num = list()
for n in range(1,10):
  if n % 2 != 0:
    num.append(n ** 2)
print(num) 

# Refazendo o code utilizando a Compreensão de Listas (list Comprehension):
num = [n ** 2 for n in range(1,10) if n % 2 != 0]
print(num)

# Aplicando 'dict Comprehension' em dicionários:

# Elevando um número de 1 a 10 a potência 2 SINTAXE NORMAL:
num = dict()
for n in range(1,11):
  num[n] = (n ** 2)
print(num)

# Refazendo o code utilizando a Compreensão de Dicionários (dict Comprehension):
num = {n: n ** 2 for n in range(1,11)}
print(num)

# Números impares de 1 a 11 elevado a potência 2 SINTAXE NORMAL:
num = dict()
for n in range(1,11):
  if n % 2 == 1:
    num[n] = (n ** 2)
print(num)

# Refazendo o code utilizando a Compreensão de Dicionários (dict Comprehension):
num = {n: n ** 2 for n in range(1,11) if n % 2 != 0}
print(num)

# Funções Lambdas (Anônimas):

# Função quadrado DECLARAÇÃO NORMAL:
def quadrado(l):
  return l * l
print(quadrado(5)) # Utilizei o print para mostrar o resultado das 2 funções(normal e lambda)

# Reescrevendo a função com a utilização de 'lambda':
quadrado2 = lambda l: l * l
print(quadrado2(8))

# Função triângulo DECLARAÇÃO NORMAL:
def tri(b, h):
  return (b * h)/2
print(tri(2,5))

# Reescrevendo a função com a utilização de 'lambda':
tri2 = lambda bh: (b * h)/2
print(tri(10,20))

# Função triplo DECLARAÇÃO NORMAL:
def triplo(t):
  return (t * 3)
print(triplo(5))

# Reescrevendo a função com a utilização de 'lambda':
trip = lambda t: (t * 3)
print(trip(5))

# Calculando o triplo de uma lista de números, DECLARAÇÃO NORMAL:
lis = [4, 5, 9, 7, 0, 1, 8]
mult = list()
res = 1
for num in lis:
  res = num * 3
  mult.append(res)
print(f'Declaração normal: {mult}')

# Calculando o triplo de uma lista de números usando o 'map':
lista = [4, 5, 9, 7, 0, 1, 8]
print(f'Usando map: {list(map(triplo, lista))}')

# Reescrevendo o code usando a função 'lambda'
print(f'Usando map e lambda: {list(map(lambda m: m * 3, [4, 5, 9, 7, 0, 1, 8]))}')

# Trabalhando com Atribuição Condicional:

# Escrevendo com DECLARAÇÃO NORMAL:
nome = 'edcarlos'
if len(nome) > 5:
  var = 100
else:
  var = 0
print(f'O valor de var é: {var}')

# Reescrevendo o code no modelo ATRIBUIÇÃO CONDICIONAL:
nome = 'edcarlos'
var = 100 if len(nome) > 5 else 0
print(f'O valor de var é: {var}')