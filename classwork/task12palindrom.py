name = input()

def palindrom(name):
    a = name[::-1]
    if name == a:
        return ('True')
    else:
        return ('False')

print(palindrom(name))