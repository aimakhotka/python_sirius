def error_alignment(i_input):
    words = ['center', 'left', 'right']
    if i_input in words:
        i_input = ['^', '<', '>'][words.index(i_input)]
    else:
        print('Ошибка в вводе типа выравнивания')
    return i_input

def error_N(i_input):
    if i_input > 0:
        return i_input
    else:
        print('Ошибка в вводе аргументов. Попробуйте снова.')

list_input = []

def user_input():
    pattern = [
        'Введите желаемый тип выравнивания (left, right or center): ', 
        'Введите желаемый символ заполнения: ',
        'Введите желаемое количество символов заполнения: ',
        'Введите аргументы через пробел: '
    ]
    count = 0
    for i in pattern:
        i_input = input(pattern[i])
        if count == 0:
            error_alignment(i_input)
        elif count == 2:
            error_N(i_input)
        elif count == 3:
            i_input = i_input.split()
        else:
            pass
        i_input += list_input
        count += 1
    return list_input


def func(list_input):
    print('{0:{1}{2}{3}}'.format(list_input[0], list_input[1], 
    list_input[2], list_input[4]))


user_input()
func(list_input)
# print('{0:{1}{2}{3}}'.format(arg[0], symbol, new_alignment, N))