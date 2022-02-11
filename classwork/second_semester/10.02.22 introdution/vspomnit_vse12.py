import random, string

def generator(n):
    s = ' '
    for i in range (n):
        s += random.choice(string.ascii_letters)
    return generator
    