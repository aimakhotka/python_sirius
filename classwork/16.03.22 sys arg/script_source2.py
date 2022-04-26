import argparse, sys, os

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--source')
parser.add_argument('-o', '--output')
args = parser.parse_args(sys.argv[1:])

def writer(filepath, dirpath):
    file_cond = os.path.exists(filepath) and os.path.isfile
    dir_cond = os.path.exists(dirpath) and os.path.isdir
    if file_cond and dir_cond:
        if dirpath[-1] != '/':
            dirpath += '/'


        with open(filepath, 'r') as f:
            lines = f.readlines()
            count = 1
            filepath = filepath[filepath.rfind('/'):]
            fn, ext = filepath.split('.')
            for line in lines:
                with open(f'{fn}_{count}.{ext}', 'w') as fw:
                    fw.write(line)
                print('Запись успешно сделана в', count, 'файл.')
                count += 1
    else:
        print('Error')

writer(filepath='/home/sirius/programming/homework_python/classwork/second_semester/16.03.22 sys arg/source.txt', dirpath='/home/sirius/programming/homework_python/classwork/second_semester/16.03.22 sys arg/output')