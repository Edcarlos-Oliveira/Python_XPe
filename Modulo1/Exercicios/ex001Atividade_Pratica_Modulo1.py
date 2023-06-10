# Declaração das Variáveis:
inicio = 100
fim = 500

# Verificando os multiplos de (2,5,7)
for n in range(inicio, fim + 1):
    if n % 2 == 0 and n % 5 == 0 and n % 7 == 0:
        print(f'{n}', end=' ')
print()


# Declaração Variável 2:
div = 100

# Verificando os divisiveis por 3:
for n2 in range(0,1000):
    if n2 % div == 0:
        print(f'{n2}', end=' ')
print()

# Declaração de Variáveis 3:
nome = 'Edcarlos Oliveira'
cidade = 'São Paulo'
cpf = '123.456.789-00'

ncpf = cpf.replace(".", "")

# Mostrando o resultado em maiusculos:
print(f'Seu nome em MAIUSCULO {nome.upper()}')
print(f'Sua cidade em MAISCULO {cidade.upper()}')
print(f'Seu nome em MINUSCULO {nome.lower()}')
print(f'Sua cidade em MINUSCULO {cidade.lower()}')
print(f'Seu nome tem {len(nome)} letras incluindo o espaço')
print(f'Sua cidade tem {len(cidade)} letras incluindo o espaço')
print(f'Removendo os "." e "-" do cpf {ncpf.replace("-", "")}')
print()

# Declaração de Variáveis 3:
numero = '127957'
soma = 0
print('A soma de ', end=" ")
for valor in numero:
    soma += int(valor)
    print(valor, end="  ")
print(f'= {soma}')    





