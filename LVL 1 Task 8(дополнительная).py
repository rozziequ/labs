import random
a = []
avg_list = []

for i in range(4):
    buffer = []
    for j in range(6):
        buffer.append(random.randint(-60, 60))
    a.append(buffer)
print('Начальная матрица:')
for i in range(4):
    print(a[i])

for i in range(4):
    sum = 0
    count = 0
    for j in range(6):
        if a[i][j] > 0:
            sum += a[i][j]
            count += 1
    avg = sum / count
    if avg == int(avg):
        avg = int(avg)
    else:
        avg = round(avg, 2)
    avg_list.append(avg)
print('Конечный массив:', avg_list)