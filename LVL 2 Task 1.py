# Дана матрица A размером 5 x 7. Для каждой строки сравнить элементы, расположенные непосредственно перед и после макс. элемента этой строки, и меньший из них увеличить в 2 раза.

import random
random.seed(416)

a = []

for i in range(5):   # Заполнение матрицы
    b = []
    for j in range(7):
            b.append(random.randint(1, 20))
    a.append(b)

print('Начальная матрица:', a)

for i in range(5):      # Нахождение макс. элемента и его индекса
    maxi = a[i][0]
    for j in range(7):
        if a[i][j] > maxi:
            maxi = a[i][j]
            index = j

    if index == 6:   # Выполнение алгоритма
        a[i][index - 1] = a[i][index - 1] * 2
    elif 0 < index < 6:
        if a[i][index - 1] < a[i][index + 1]:
            a[i][index - 1] = a[i][index - 1] * 2
        elif a[i][index - 1] > a[i][index + 1]:
             a[i][index + 1] = a[i][index + 1] * 2
        elif a[i][index - 1] == a[i][index + 1]:
             a[i][index - 1] = a[i][index - 1] * 2
             a[i][index + 1] = a[i][index + 1] * 2
    elif index == 0:
         a[i][index + 1] = a[i][index + 1] * 2

print('Конечная матрица:', a)