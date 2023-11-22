text = input('Введите текст:')
result = ""
inside_bracket = False

for char in text:
    if char == '(':
        inside_bracket = True
        result += '('
    elif char == ')':
        inside_bracket = False
        result += ')'
    elif inside_bracket:
        result += ''
    else:
        result += char

print(result)