# Вводя n значений r, вычислить по выбору площадь квадрата со стороной r, площадь круга радиусом r или площадь равностороннего треугольника со стороной r. Использовать множественный выбор.

import math

r = 0
a = 0
exp_a = 0
while exp_a <= 0 or exp_a != int(exp_a):
    exp_a = int(input('Сколько расчетов по r будет проведено: '))
    print()
    if exp_a <= 0 or exp_a != int(exp_a):
        print('Пожалуйста, введите корректное значение.') 
        print()
    else:
        break

while a < exp_a:

    print('1) Площадь квадрата')
    print('2) Площадь равностороннего треугольника')
    print('3) Площадь круга')
    print()
    var = int(input('Введите ваш вариант: '))

    if var > 3 or var < 1:
        print('Пожалуйста, введите корректный вариант')
        print()
        continue

    r = input('Введите значение r: ')
    
    if int(r) < 0:
        print('Введите корректное значение r')
        print()
        continue
    
    elif var == 1:
        s = int(r) ** 2
        print('Площадь квадрата равна', s)
        print()
    
    elif var == 2:
        s = (math.sqrt(3) * int(r) ** 2) / 4
        print('Площадь равностороннего треугольника приблизительно равна', round(s, 3))
        print()
    
    elif var == 3:
        s = math.pi * int(r) ** 2
        print('Площадь круга приблизительно равна равна', round(s, 3))
        print()

    a = a + 1
    
print('Заданное количество операций обработано. Программа завершила свою работу.')