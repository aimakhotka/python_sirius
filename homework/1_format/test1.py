list_input = []

def error_alignment(i_input):
    words = ['center', 'left', 'right']
    if i_input in words:
        i_input = ['^', '<', '>'][words.index(i_input)]
    else:
        print('Ошибка в вводе типа выравнивания')
    return i_input

def error_N(i_input):
    if int(i_input) > 0:
        return i_input
    else:
        print('Ошибка в вводе аргументов. Попробуйте снова.')

pattern = [
        'Введите желаемый тип выравнивания (left, right or center): ', 
        'Введите желаемый символ заполнения: ',
        'Введите желаемое количество символов заполнения: ',
        'Введите аргументы через пробел: '
    ]
count = 0
for i in range(len(pattern)):
    i_input = input(pattern[i])
    if count == 0:
        error_alignment(i_input)
    elif count == 1:
        pass
    elif count == 2:
        error_N(i_input)
    elif count == 3:
        i_input = i_input.split()
    else:
        pass
    list_input += i_input
    count += 1
print(list_input)