import os

def islinux():

    b = os.uname()
    print(b.sysname, b.version)
    return b.sysname == 'Linux'

print(islinux())