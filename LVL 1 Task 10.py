x = float(input('Введите значение аргумента: '))
y = 0

if x <= -1:   # Условие 1
    y = 1
    print('y =', y)

elif x == 0: # Исключение ответа x = -0.0
    y = 0
    print('y =', y)

elif x == 1: # Исключение ответа -1.0
    y = -1
    print('y =', y)

elif -1 < x <= 1:  # Условие 2
    y = -x
    print('y =', y)

else:    # Условие 3
    y = -1
    print('y =', y)