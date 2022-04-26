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
        i_input = input(i)
        if count == 0:
            error_alignment(i_input)
        elif count == 2:
            error_N(i_input)
        elif count == 3:
            i_input = i_input.split()
        else:
            pass
        list_input.append(i_input)
        count += 1
    return list_input


def func(*list_input):
    for i in list_input[3]:
        print('{0:{1}{2}{3}}'.format(i, list_input[1], list_input[0], list_input[2]))

# print(user_input())
# print(list_input)
func(user_input())
# print('{0:{1}{2}{3}}'.format(arg[0], symbol, new_alignment, N))