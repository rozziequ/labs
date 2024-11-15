import math
k = 5

def comb(n):
    comb = math.factorial(n)/(math.factorial(k) * math.factorial(n - k))
    return int(comb)

x1 = 8
x2 = 10
x3 = 11

print('Существует', comb(x1), 'способов отобрать 5 человек из', x1, 'кандидатов')
print('Существует', comb(x2), 'способов отобрать 5 человек из', x2, 'кандидатов')
print('Существует', comb(x3), 'способов отобрать 5 человек из', x3, 'кандидатов')