from random import randrange

def show(func):
    def new_func(*args, **kwargs):
        print('Running function: ', func.__name__)
        print('Positional arguments are: ', args)
        print('Keyword arguments are: ', kwargs)
        result = func(*args, **kwargs)
        return result
    return new_func
        
def initials(name):
    l = name.split()
    return l[0] +' ' + l[1][0:1] + '. ' + l[2][0:1] + '.'

@show
def initials_more(names):
    return [initials(name) for name in names]

def initials_multiply(name, num):
    return [name for i in range(num)]

print(initials_more(initials_multiply('Махотка Алла Ивановна', 3)))
