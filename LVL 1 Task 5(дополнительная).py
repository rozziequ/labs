# Вычислить скалярное произведение двух векторов размером 4

import random

a = []
b = []

for i in range(4):
    a.append(random.randint(-20, 20))
    b.append(random.randint(-20, 20))

print('a =', a)
print('b =', b)
print()

prod_ab = 0
for i in range(4):
    prod_ab = prod_ab + a[i] * b[i]

print('Скалярное произведение a и b равно', prod_ab)