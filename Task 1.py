# Вычислить при заданном x сумму s = 1 + 1/x + 1/x^2 + ... + 1/x^10

import math

x = int(input('Введите значение x: '))
s = 0
for i in range(10):
    s += 1 / pow(x, i)

print('s =', round(s, 3))