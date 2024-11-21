# Для каждой из трёх заданных матриц найти среднее значение её элементов без учета макс. и мин. элементов. Полученные значения занести в одномерный массив.
# Определить, образовали ли полученные значения убывающую последовательность. Нахождение среднего значения элементов оформить в виде метода.

import random

totalmatrix = []

def avgfunc(x, stringsfunc, columnsfunc, totalfunc):
    maxifunc = x[0][0]
    minifunc = x[0][0]

    for i in range(stringsfunc):
        for j in range(columnsfunc):
            if maxifunc < x[i][j]:
                maxifunc = x[i][j]
            if minifunc > x[i][j]:
                minifunc = x[i][j]

    sum = 0
    count = 0

    for i in range(stringsfunc):
        for j in range(columnsfunc):
            if x[i][j] != maxifunc and x[i][j] != minifunc:
                sum += x[i][j]
                count += 1
    avg = sum / count
    if avg == int(avg):
        totalfunc.append(int(avg))
        avg = int(avg)
    else:
        totalfunc.append(round(avg, 2))
        avg = round(avg, 2)
    print('Среднее значение матрицы без учета максимального и минимального элемента равно:')
    return avg

a = []
strings_a = random.randint(2, 6)
columns_a = random.randint(2, 6)
b = []
strings_b = random.randint(2, 6)
columns_b = random.randint(2, 6)
c = []
strings_c = random.randint(2, 6)
columns_c = random.randint(2, 6)

for i in range(strings_a):
    buff = []
    for j in range(columns_a):
        buff.append(random.randint(1, 60))
    a.append(buff)

for i in range(strings_b):
    buff = []
    for j in range(columns_b):
        buff.append(random.randint(1, 60))
    b.append(buff)

for i in range(strings_c):
    buff = []
    for j in range(columns_c):
        buff.append(random.randint(1, 60))
    c.append(buff)

print(avgfunc(a, strings_a, columns_a, totalmatrix))
print(avgfunc(b, strings_b, columns_b, totalmatrix))
print(avgfunc(c, strings_c, columns_c, totalmatrix))
print()
print('Конечная матрица с средними значениями заданных матриц(без учёта макс. и мин. элементов):', totalmatrix)

if totalmatrix[0] < totalmatrix[1] < totalmatrix[2]:
    print('Последовательность является возрастающей')
elif totalmatrix[0] > totalmatrix[1] > totalmatrix[2]:
    print('Последовательность является убывающей')
else:
    print('Последовательность является ни возрастающей, ни убывающей')