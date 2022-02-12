alignment = input('Введите желаемый тип выравнивания \
(left, right or center): ') #тип выравнивания
symbol = input('Введите желаемый символ заполнения: ')
N = input('Введите желаемое количество символов заполнения: ') #кол-во символов заполнения
arg = input('Введите аргументы через пробел: ').split() #принимаем аргументы и создаем из них список

words = ['center', 'left', 'right']
if alignment in words:
    new_alignment = ['^', '<', '>'][words.index(alignment)]
else:
    print('Ошибка в вводе типа выравнивания')

def func(arg, new_alignment, N, symbol):
    for i in arg:
        print('{0:{1}{2}{3}}'.format(i, symbol, new_alignment, N))

func(arg, new_alignment, N, symbol)
