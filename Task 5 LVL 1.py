'''
Уровень 1 Задание 5
'''

import math
from random import *

seed(1)
p = randint(1, 10)
seed(2)
h = randint(1, 10)
s = pow(p, 2)

for i in range (1, 10):
    s = s + pow((p + i * h), 2)

print(s)
