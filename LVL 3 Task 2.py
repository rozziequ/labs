# В заданной матрице расположить элементы четных строк в порядке возрастания, а элементы нечетных строк - в порядке убывания.
# Обработку матрицы по строкам осуществлять в методе.

import random

def matrix_func(x, string_func, column_func):
    for i in range(string):
        if i % 2 == 1:
            for k in range(column_func):
                for j in range(column_func - 1):
                    if x[i][j] > x[i][j + 1]:
                        x[i][j], x[i][j + 1] = x[i][j + 1], x[i][j]
        if i % 2 == 0:
            for k in range(column_func):
                for j in range(column_func - 1):
                    if x[i][j] < x[i][j + 1]:
                        x[i][j], x[i][j + 1] = x[i][j + 1], x[i][j]

    print("Матрица после преобразований:")
    for i in range(string_func):
        print(x[i])

a = []
string = random.randint(3, 6)
column = random.randint(4, 8)

for i in range(string):
    buff = []
    for j in range(column):
        buff.append(random.randint(-40, 40))
    a.append(buff)
    
print("Изначальная матрица:")
for i in range(string):
    print(a[i])

print()
matrix_func(a, string, column)