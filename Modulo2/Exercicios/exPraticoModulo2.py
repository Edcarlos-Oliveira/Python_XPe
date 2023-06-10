# Atividade Prática Módulo 2:
import numpy as np
import pandas as pd

# == CÓDIGO 1 == #
z = np.zeros((4, ))
print(f'Valor de z: {z}')
print()

# == CÓDIGO 2 == #
z = np.zeros((4, ))
z[1] = 1
print(f'Valor de z: {z}')
print()

# == CÓDIGO 3 == #
z = np.zeros((4, ))
z[1:] = 1
print(f'Valor de z: {z}')
print()

# == CÓDIGO 4 == #
z = np.zeros((4, ))
z[:-1] = 1
print(f'Valor de z: {z}')
print()

# == CÓDIGO 5 == #
lista = [[2, 2], [2, 2]]
x = np.array(lista)
print(f'Valor de x:\n {x}')
print()

# == CÓDIGO 6 == #
x = np.array([[1, 2], [3, 4]])
y = x[0, :]
y[1] = 10
print(f'Valor de x:\n {x}')
print()

# == CÓDIGO 7 == #
x = np.array([[1, 3], [11, 10]])
print(f'Valores de x:\n {x}')
print(f'A média de x: {np.mean(x[x > np.pi])}') # 'np.pi' valor de 'pi'
print()

# == CÓDIGO 8 == #
data = {'animal':['cat', 'cat', 'snake', 'dog',
         'cat', 'snake', 'cat', 'dog', 'dog'],
         'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
         'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
         'priority': ['yes', 'yes', 'no', 'yes', 'no',
                      'no', 'no', 'yes', 'no', 'no'  ]}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(data)
print()
print(labels)

# == CÓDIGO 9 == #
df = pd.DataFrame(data=data, index=labels)

# == CÓDIGO 10 == #
y_true = np.array([1., 2., 1.])
y_pred = np.array([1.1, 1.98, 1.05])

print(y_true)
print(y_pred)
