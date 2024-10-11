from random import *

n = 30
seed(7)
norm = randint(10, 50)  # Проходное значение норматива
total = 0
print('Значение норматива', norm)

for i in range(n):
    x = int(input('Результат норматива: '))
    if x >= norm:
        total += 1

print(total)

