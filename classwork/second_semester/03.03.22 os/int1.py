import os
import subprocess

def hw():
    commands = subprocess.getoutput('cat ~/.bash_history').split('\n')
    ind, counter, counter2 = True, len(commands) - 1, 0
    print('y == выполнить, n == далее, q = выйти')
    while ind:
        print(f'command {1+counter2}: ', commands[counter])
        answ = input()
        ind = answ != 'q'
        if answ[0].lower() == 'y':
            os.system(commands[counter])
        counter -= 1
        counter2 += 1

hw()