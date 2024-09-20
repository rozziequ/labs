'''
Уровень 3 Задание 8
'''
import math
a = 0.1
b = 1
h = 0.05
s = 0
i = -1
x = a
n = (b - a) // h

while x <= b:
    i += 1
    si = pow((2 * x), i) / math.factorial(i)
    if si < 0.0001:
        break
    print('y =', round(math.exp(2 * x), 2))
    while i <= n:
        si = pow((2 * x), i) / math.factorial(i)
        s = s + si
        print('s =', round(s, 2))
        break
    x += h
    print()
