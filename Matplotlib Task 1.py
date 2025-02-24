import matplotlib.pyplot as plt
import numpy as np

a = int(input('Введите коэффицент a:'))
b = int(input('Введите коэффицент b:'))
c = int(input('Введите коэффицент c:'))

x = np.arange(-10, 10)

f = a+b/x+c*x/(1+x)

x != -1
x != 0

plt.plot(x, f)
plt.show()