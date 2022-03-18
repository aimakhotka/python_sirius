import tarfile

f = open('new.txt', 'w')
s = 'This is the test string'
for i in range(10000):
    f.write(s+'\n')
    print(i)
f.close()

t = tarfile.open('new.tar.gz', 'w|gz')
t.add('new.txt')
t.close()