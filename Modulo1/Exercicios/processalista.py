# Ex005 Modulo Python com números inteiros:

#Encontra e retorna o maior número impar presente na lista:

def maior_impar(lista):
    maior = lista[0]
    for m in lista:
        if m % 2 != 0:
            if m > maior:
                maior = m              
    return maior

#Encontra e retorna o menor número impar presente na lista:
def menor_impar(lista):
    menor = lista[0]
    for mn in lista:
        if mn % 2 != 0:
            if mn < menor:
                menor = mn
    return menor

#Encontra e retorna o maior e menor número impar presente na lista:
def maior_menor(lista):
    maior = menor = lista[0]
    for mm in lista:
        if mm % 2 != 0:
            if mm > maior:
                maior = mm
            if mm < menor:
                menor = mm
    return (maior, menor)
