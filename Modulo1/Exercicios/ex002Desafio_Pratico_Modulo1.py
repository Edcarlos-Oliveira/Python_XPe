import processalista

# Ex001 Relação de Nomes:
nomes = ['Maria', 'Julieta', 'Fernando', 'Cristiano', 'Julieta', 'Maria', 'Fernando', 'Cláudio']
qtd_letras = {}
for nome in nomes:
    qtd_letras[nome] = len(nome)
print(qtd_letras)

# Ex002 Reescrevendo o código(Ex001) usando 'dict Comprehension':
nomes = ['Maria', 'Julieta', 'Fernando', 'Cristiano', 'Julieta', 'Maria', 'Fernando', 'Cláudio']
qtd_letras = {nome: len(nome) for nome in nomes}
print(f'Escrevendo com dict comprehension: {qtd_letras}')

# Ex003 Criando uma função 'area(r, pi), que calcule a área de um círculo:
def area(r, pi=3.14159265359):
    return pi * (r ** 2) 
print(f'A área do circulo é: {area(5)}')

# Ex004 Reescrevendo o código com a função 'lambda':
area = lambda r, pi: pi * (r ** 2)
print(f'Área do circulo usando lambda: {area(5, 3.14)}')

# Ex005 Modulos em Python (Importando o arquivo das funções 'processalista'):
lista = [15, 2, 30, 4, 5, 6, 7, 8, 9, 10]
print(f'O MAIOR número impar da lista é: {processalista.maior_impar(lista)}')
print(f'O MENOR número impar da lista é: {processalista.menor_impar(lista)}')
print(f'O MAIOR e MENOR número impar da lista é: {processalista.maior_menor(lista)}')

#Ex006 Escala Médicos:
# Relação de cada dia da semana que cada médico atende:
cardiologista = {'terca', 'quinta'}
ortopedista = {'terca', 'quinta'}
dermatologista = {'segunda', 'quinta', 'sexta'}
neurologista = {'terca', 'quinta', 'sexta'}
psiquiatra = {'segunda', 'quarta', 'sexta'}

# Unindo todos os conjuntos:
especialistas = cardiologista | ortopedista | dermatologista | neurologista | psiquiatra
print(f'Dias que tem médicos: {especialistas}')

def disp_dois_especialistas(med01, med02):
    return ortopedista & neurologista
print(f'Para duas especialidades: {disp_dois_especialistas(ortopedista, neurologista)}')

def disp_tres_especialistas(med01, med02, med03):
    return psiquiatra & neurologista & dermatologista
print(f'Para três especialidades: {disp_tres_especialistas(dermatologista, neurologista, psiquiatra)}')



