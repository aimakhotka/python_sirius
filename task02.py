names = ['Makhotka Alla Ivanovna', 'Ivanov Ivan Ivanovich']
def initials (name):
    result = name.split()
    return result[0] + '. ' + result[1][0:1] + '. ' + result[2][0] + '.'

def initials_more (names):
    result = []
    return [initials(name) for name in names]

print(initials_more(names))
