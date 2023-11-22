text = input('Введите текст: ') + ' '
list = []
for i in range(len(text)):
    for j in range(i, len(text)):
        if text[j] == ' ' and text[i:j] != '':
            list += [text[i:j]]
            i = j + 1
    break
print(list)
count = 0
for element in list:
    if element.count('а') >= 2:
        count += 1
print('Кол-во слов с двумя и более буквами ' 'а'': ' + str(count))