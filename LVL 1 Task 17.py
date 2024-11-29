# В каждой строке матрицы B размером n x m минимальный элемент поместить в начало строки, сохранив порядок остальных элементов.

import random
mini = 0
a = []

height = random.randint(2, 4)  # Количество строк
width = random.randint(3, 6)   # Количество столбов

for i in range(height):   # Заполнение массива
    b = []
    for j in range(width):
        b.append(random.randint(1, 20))
    a.append(b)

print('Начальная матрица:')
for i in range(height):
    print(a[i])

for i in range(height):
    mini = a[i][0]
    for j in range(width):
        if a[i][j] < mini:
            mini = (a[i][j])
    for j in range(width):
        if mini == a[i][j]:
            a[i].pop(j)
            a[i].insert(0, mini)

          
print('Конечная матрица:')
for i in range(height):
    print(a[i])