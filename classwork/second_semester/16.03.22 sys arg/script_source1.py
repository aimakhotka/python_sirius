
def writer(filepath):

    with open(filepath, 'r') as f:
            lines = f.readlines()
    with open(filepath, 'w') as f:
        count = 1
        for line in lines:
            output_path = filepath + '_{0}'.format(count)
            file = open(output_path, 'w')
            file.write(line)
            file.close
            print('Запись успешно сделана в', count, 'файл.')
            count += 1

writer(filepath='source')