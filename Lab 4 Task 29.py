# В матрице F размером 5 x 7 удалить столбец, расположенный после столбца, содержащего минимальный по модулю элемент во 2-й строке.
import random

F = []

for i in range(5):
    buff = []
    for j in range(7):
        buff.append(random.randint(-9, 9))
    F.append(buff)

print('Изначальная матрица:')
for i in range(5):
    print(F[i])


for i in range(1, 2):
    mini = F[i][0]
    mini_index = 0
    for j in range(7):
        if abs(F[i][j]) < abs(mini):
            mini = F[i][j]
            mini_index = j

print()
print('Минимальный(-ые) элемент(-ы) во 2-й строке:', abs(mini))
mini_matrix = []
for i in range(1, 2):
    for j in range(7):
        if F[i][j] == mini:
            mini_matrix.append(j)

len_mini_matrix = len(mini_matrix)
for n in range(len_mini_matrix):
    if mini_matrix[n * (-1)] == 6:
        continue
    else:
        for j in F:
            j.pop(mini_matrix[n * (-1)] + 1)

print()
print('Конечная матрица после преобразований:')
for i in range(5):
    print(F[i])