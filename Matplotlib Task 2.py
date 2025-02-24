import matplotlib.pyplot as plt

file = open('D:\OneDrive\Документы\Lab Matplotlib\Data.txt', 'r')
x = file.readline()
y = file.readline()

x_split = x.split(' ' or '\n')
y_split = y.split(' ' or '\n')
x_float = []
y_float = []
for i in range(len(x_split)):
    buff = float(x_split[i])
    x_float.append(buff)
for i in range(len(y_split)):
    buff = float(y_split[i])
    y_float.append(buff)
print(x_float)
print(y_float)

plt.plot(x_float, y_float)
plt.show()