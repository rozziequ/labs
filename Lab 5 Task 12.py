# Заданы две матрицы одинакового размера. Столбец 1-ой матрицы, содержащий макс. элемент матрицы, поменять со столбцом второй матрицы, содержащим макс. элемент.
# Поиск столбца, содержащего макс. элемент матрицы, оформить в виде метода.
import random

def findmaxi(x, stroks, stolbs):         # Метод для нахождения максимального элемента матрицы и его индекса

    maxi_x = x[0][0]
    x_index = 0
    for i in range(stroks):
        for j in range(stolbs):
            if x[i][j] > maxi_x:
                maxi_x = x[i][j]
                x_index = j
    print(x_index)
    return x_index
            
a = []
b = []
string = random.randint(3, 4)
column = random.randint(3, 4)

for i in range(string):            # Формируем матрицы со случайными значениями
    buff = []
    for j in range(column):
        buff.append(random.randint(1, 999))
    a.append(buff)

for i in range(string):
    buff = []
    for j in range(column):
        buff.append(random.randint(1, 999))
    b.append(buff)

print("Изначальная матрица А:")
for i in range(string):
    print(a[i])

print()
print("Изначальная матрица В:")
for i in range(string):
    print(b[i])

print()
print("Индекс столбца с макс. элементом матрицы А:")
a_index = findmaxi(a, string, column)
print("Индекс столбца с макс. элементом матрицы B:")
b_index = findmaxi(b, string, column)

a_buff = []
for i in range(string):
    a_buff.append(a[i][a_index])
b_buff = []
for i in range(string):
    b_buff.append(b[i][b_index])

for j in a:
    del j[a_index]
for j in b:
    del j[b_index]

for i in range(string):
    b[i].insert(b_index, a_buff[i])

for i in range(string):
    a[i].insert(a_index, b_buff[i])

print()
print("Конечная матрица А:")
for i in range(string):
    print(a[i])

print()
print("Конечная матрица В:")
for i in range(string):
    print(b[i])