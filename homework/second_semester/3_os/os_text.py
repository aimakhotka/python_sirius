import os

pathh = input('Введите название файла: ')
text1 = input('Введите текст, который необходимо заменить: ')
text2 = input('Введите текст для замены: ')
abs_path = os.path.abspath(pathh)


def swap(abs_path, pathh, text1, text2):
    if not os.path.exists(abs_path):
        print(os.path.exists(abs_path))
        print('Путь не существует')
    elif not os.path.isfile(abs_path):
        print('Это не файл')
    elif not abs_path[-4:] == '.txt':
        print(abs_path[-4:])
        print('Неверное расширение')
    else:
        with open(pathh, 'r') as file:
            data = file.read()
        with open(pathh, 'w') as file:
            data = data.replace(text1, text2)
            file.write(data)
        print('Запись успешно сделана.')

swap(abs_path, pathh, text1, text2)