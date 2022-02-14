alignment = input('Введите желаемый тип выравнивания \
(left, right or center): ') #тип выравнивания
symbol = input('Введите желаемый символ заполнения: ') #символ заполнения
N = int(input('Введите желаемое количество символов заполнения: ')) #кол-во символов заполнения
arg = input('Введите аргументы через пробел: ').split() #принимаем аргументы и создаем из них список



def func(arg, alignment, N, symbol):
    if N <= 0:
        print('Количество символов заполнения должно быть больше нуля.')

    for i in arg:
        if len(i) > N:
            print('Длина каждого аргумента не должна превышать количество символов заполнения.')
    
    words = ['center', 'left', 'right']
    if alignment in words:
        new_alignment = ['^', '<', '>'][words.index(alignment)]
        for i in arg:
            print('{0:{1}{2}{3}}'.format(i, symbol, new_alignment, N))
    else:
        print('Ошибка в вводе типа выравнивания')


func(arg, alignment, N, symbol)
