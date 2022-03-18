import tarfile

# ls -l | grep name
# метаданные файла

# t = tarfile.open('archive.tar', 'w')
t = tarfile.open('archive.tar.gz', 'w|gz')
t.add('1.txt')
t.close