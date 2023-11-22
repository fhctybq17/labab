mod = []
n = input('Кол-во элементов: ')
try:
    n = int(n)
    while n != 0:
        n -= 1
        spisok += [random.randint(-100,100)]
    print('Список: ' + str(spisok))
    for i in range(len(spisok)):
        if spisok[i] < 0:
            mod += [int(str(spisok[i])[1:])]
        else:
            mod += [int(str(spisok[i]))]
    for i in range(100, 0, -1):
        if i in mod:
            max = i
            break
    num = 0
    for i in mod:
        if i != max:
            num += 1
        elif i == max:
            num += 1
            break
    print('Номер максимального элемента: ' + str(num))
    spis = []
    sres = 0
    summa = 0
    for i in spisok:
        if i <= 0:
            sres += 1
        elif i > 0:
            sres += 1
            break
    spis = mod[sres:]
    for i in spis:
        summa += i
    print('Сумма модулей элементов после первого положительного: ' + str(summa))
except:
    print('Введите натуральное число')