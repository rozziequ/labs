import random

a = []
len = random.randint(5, 8)
for i in range(len):
    a.append(random.randint(1, 15))

print('Изначальный массив', a)
print()

min = a[0]
for i in range(1, len):
    if a[i] < min:
        min = a[i]
        min_numb = i
print('Минимальный элемент равен', min)
print()

print('Тестирование:')
exp_min = 1
exp_min_numb = 7
if exp_min == min and exp_min_numb == min_numb:
    print('Верно!')
else:
    print('Программа работает некорректно!')
print()

for i in range(len):  # На случай, если будет несколько одинаковых минимальных элементов
    if min == a[i]:
        a[i] = a[i] * 2        

print('Конечный массив после преобразований:', a)
