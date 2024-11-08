import random

len = 5
a = []

for i in range(len):    # Заполнение массива
    a.append(random.randint(1, 20))
print('Элементы начального массива:', a)
print()

sum = 0   # Вычисление среднего значения элементов массива
for i in range(len):
    sum = sum + a[i] 
avg = sum / len
print('Среднее значение элементов массива равно', int(avg))
print()

for i in range(len):  # Преобразование массива
    if a[i] - avg == int(a[i] - avg):  # Исключение лишних знаков после запятой
        a[i] -= avg
        a[i] = int(a[i])
    else: 
        a[i] = round(a[i] - avg, 1)

print('Элементы конечного массива:', a)
