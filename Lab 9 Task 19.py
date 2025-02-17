# Сформировать массив из положительных элементов заданного массива размером 10.

file = open('D:/OneDrive/Документы/Lab 9/Lab 9.txt', 'r')
s = file.read()   # Считывание текста
print('Изначальный текст:', s)
s_split = s.split()
print('Преобразование в массив:', s_split)
len_s_split = len(s_split)  # Количество элементов массива
for i in range(10):
    s_split[i] = int(s_split[i])   # Преобразование строковых элементов в целочисленные
print('Целочисленный массив:', s_split)

maxx = s_split[0]
for i in range(len_s_split):
    if s_split[i] > maxx:
        maxx = s_split[i]

sum = 0
for i in range(len_s_split):
    if s_split[i] != maxx:
        sum += s_split[i]
if maxx > sum:
    for i in range(len_s_split):
        if s_split[i] == maxx:
            s_split[i] = 0
else:
    for i in range(len_s_split):
        if s_split[i] == maxx:
            s_split[i] = 2 * s_split[i]

print('Конечный результат:', s_split)