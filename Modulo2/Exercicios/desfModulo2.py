# Importando as bibliotecas:
import numpy as np
import pandas as pd

# Lendo o arquivo csv:
df = pd.read_csv('https://pycourse.s3.amazonaws.com/bike-sharing.csv')
print()

# Tamanho do dataset(tds):
tds = len(df) 
print(f'Tamanho do dataset: {tds} cadastros.')
print()

# Média da coluna 'windspeed(velocidade do vento entre 0 e 1)[cw]'
cw = df['windspeed'] 
print(f'A média da coluna windspeed: {np.mean(cw)}')
print()

# Média da coluna 'temp(Temperatura escalada de 0 e 1)[ct]'
ct = df['temp'] # 'ct' coluna temp
print(f'A média da coluna temp: {np.mean(ct)}')
print()

# Quantos registros existem para o ano 2011(a_2011):
a_2011 = df[df['year'] == 0]
print(f'A quantidade de registros em 2011: {len(a_2011)}')
print()

# Quantos registros existem para o ano de 2012(a-2012):
a_2012 = df[df['year'] == 1]
print(f'A quantidade de registros em 2012: {len(a_2012)}')
print()

# Quantas locações foram efetuadas em 2011, 'total_count (quantidade de locações casuais e registrados)[lb]'
lb_2011 = df[df['year'] == 0] # locações bicicletas
print(f'O total de locações em 2011: {np.sum(lb_2011["total_count"])}')
print()

# Quantas locações foram efetuadas em 2012, 'total_count (quantidade de locações casuais e registrados)[lb]'
lb_2012 = df[df['year'] == 1]
print(f'O total de locações em 2012: {np.sum(lb_2012["total_count"])}')
print()
# Qual estação do ano contém maior e menor média de locações(ml)
mai = men = 0
for c in range(1, 5):
    est = df[df['season'] == c]
    m = np.mean(est['total_count'])
    if c == 1:
        mai = men = m
        e_mai = e_men = c 
    elif m > mai:
        mai = m
        e_mai = c
    elif m < men:
        men = m
        e_men = c
print(f'Na estação {e_mai} tem as maiores médias de locações: {mai}')
print(f'Na estação {e_men} tem as menores médias de locações: {men}')
print()

# Qual o horário do dia(hd) contém a maior e menor média de locações(hour)
mai = men = 0
for c in range(0, 24):
    hd = (df[df['hour'] == c])
    m = (np.mean(hd['total_count']))
    if c == 0:
        mai = men = m
        h_mai = h_men = c 
    elif m > mai:
        mai = m
        h_mai = c
    elif m < men:
        men = m
        h_men = c   
print(f'Às {h_mai} h(s) tem a maior média de locações: {mai}')
print(f'Às {h_men} h(s) tem a menor média de locações: {men}')
print()

# Qual dia da semana contém maior e menor média de locação:
mai = men = 0
for c in range(0,7):
    ds = (df[df['weekday'] == c])
    m = (np.mean(ds['total_count']))
    if c == 0:
        mai = men = m
        d_mai = d_men = c
    elif m > mai:
        mai = m
        d_mai = c
    elif m < men:
        men = m
        d_men = c
print(f'O dia {d_mai} da semana com maior média de locações: {mai}')
print(f'O dia {d_men} da semana com menor média de locações: {men}')
print()

# Qual horário das quartas-feiras tem maior média de locações:
mai = 0
d = df[df['weekday'] == 3]
for c in range(0, 24):
    h = d[d['hour'] == c]
    m = (np.mean(h['total_count']))
    if c == 0:
        mai = m
        hr_mai = c
    elif m > mai:
        mai = m
        hr_mai = c 
print(f'Às {hr_mai} h(s) das quartas-feiras tem maior média de locações: {mai}')
print()

# Qual horário do sábado tem maior média de locações:
mai = 0
d = df[df['weekday'] == 6]
for c in range(0, 24):
    h = d[d['hour'] == c]
    m = (np.mean(h['total_count']))
    if c == 0:
        mai = m
        hr_mai = c
    elif m > mai:
        mai = m
        hr_mai = c
print(f'Às {hr_mai} h(s) dos sábados tem maior média de locações: {mai}')
    




    
    
    
    

   


