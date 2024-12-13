# Минимальный элемент заданного одномерного массива увеличить в 2 раза.

import random

a = []
len = random.randint(5, 8)
for i in range(len):
    a.append(random.randint(1, 15))

print('Изначальный массив', a)
print()

min = a[0]
for i in range(1, len):
    if a[i] < min:
        min = a[i]
        min_numb = i
print('Минимальный элемент равен', min)
print()

for i in range(len):  # На случай, если будет несколько одинаковых минимальных элементов
    if min == a[i]:
        a[i] = a[i] * 2        

print('Конечный массив после преобразований:', a)
