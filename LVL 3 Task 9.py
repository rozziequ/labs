import random
random.seed(7)

a = []
b = []
len_a = random.randint(5, 10)
len_max = 0
len = 0
for i in range(len_a):    # Заполнение массива
    a.append(random.randint(1, 20))

for i in range(len_a - 1):
    b.append((a[i + 1]))

for i in range(len_a - 1):
    if b[i] > a[i]:
        len += 1
    elif b[i] < a[i]:
        len_max = len

print("Максимальная длина посследовательности:", len_max + 1)