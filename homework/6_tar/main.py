import tarfile

def archive():
    # print(pathh)
    path = '/home/sirius/github/python_sirius/homework/6_tar/test/'
    path_tar = 'test'
    with tarfile.TarFile.open('/home/sirius/github/python_sirius/homework/6_tar/sample.tar.gz', 'w:gz') as tar:
        tar.add(path, path_tar)
    print('Архив успешно создан.')
    
    with tarfile.TarFile.open('/home/sirius/github/python_sirius/homework/6_tar/sample.tar.gz') as tar:
        infos = tar.getmembers()
        for inf in infos:
            print(inf.name)

archive()