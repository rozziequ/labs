# Все отрицательные элементы массива перествить в конец с сохранением порядка их следования

import random
random.seed(1016)

a = []
b = []
len = random.randint(5, 10)

for i in range(len):
    a.append(random.randint(-30, 30))
print('Начальный массив:', a)

s = 0
for j in range(len):
    if a[j] < 0:
        b.append(a[j])
        s += 1

i = 0
count = s
while len >= count:
    if a[i] < 0:
        a.pop(i)
    i = i + 1
    count = count + 1
    
for i in range(s):
    a.append(b[i])

print('Конечный массив:', a)
