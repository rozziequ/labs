import math
p = int(input())
h = int(input())
s = pow(p, 2)

for i in range (1, 10):
    s = s + pow((p + i * h), 2)

print(s)