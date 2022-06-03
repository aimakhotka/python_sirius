import os
import subprocess

def search():
    output = subprocess.getoutput('cat ~/.bash_history').split('\n')
    keyword = input('Поиск по истории команд Bash. \nВвод: ').lower()

    result = []
    for i in output:
        if keyword in i:
            result.append(i)

    
    num = len(result)
    if num == 0:
        print('Соответствия не найдены.')
    else:
        print(f"Найдено {num} соответствий. Нажмите 'y' для выполнения команды, 'n' для перехода к следующей команде, 'q' чтобы выйти")
        for i in range(num):
            print(result[i])
            answ = input().lower()
            if answ == 'y':
                os.system(result[i])
                answ2 = input('Команда выполнена успешно. Выйти?\n').lower()
                if answ2 == 'y' or answ2 == 'q':
                    break
            if answ == 'q':
                break

search()