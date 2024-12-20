# Составить программу для обработки результатов кросса на 500 м для женщин. Для каждой участницы ввести фамилию, группу, фамилию преподавателя, результат.
# Получить результирующую таблицу, упорядоченную по результатам, в которой также содержится информация о выполнении норматива. Определить суммарное количество участниц, выполнивших норматив.

class Cross:
    def __init__(self, surname, group, prepod_surname, result):
        self.surname = surname
        self.group = group
        self.prepod_surname = prepod_surname
        self.result = result

a = []
n = 0
stopbro = ''
while stopbro != 'СТОП':
    buff = Cross(input('Введите фамилию участницы(для завершения ввода оставьте ХОТЯ БЫ ОДНО из полей пустым): '), input('Введите номер группы: '), input('Введите фамилию преподавателя: '), input('Введите результат в секундах: '))
    if buff.surname == '' or buff.group == '' or buff.prepod_surname == '':
        stopbro = 'СТОП'
        break
    buff.result = int(buff.result)
    a.append(buff)
    n += 1

norm = 110
print()
print('Норматив:', norm, 'секунд')
norm_pass = 0

for i in range(n - 1):
    for j in range(0, n - i - 1):
            if a[j + 1].result < a[j].result:
                a[j], a[j + 1] = a[j + 1], a[j]
for i in range(n):
    if a[i].result <= norm:
        norm_pass += 1

print('Суммарное количество участников, выполнивших норматив:', norm_pass)
print()
for i in range(n):
    print('Фамилия:', a[i].surname, '| Группа:', a[i].group, '| Преподаватель:', a[i].prepod_surname, '| Результат:', a[i].result)