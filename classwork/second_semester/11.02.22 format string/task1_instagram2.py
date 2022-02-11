# Функция для инстаграма
# Принимает список пользователей
# 1: us1 likes it 
# 2: us 1 and us2 like it 
# 3: us1, us2 and us3 like it
# 4: us 1 and n-1 like it 

s = ['us1', 'us2', 'us3']
def insta(s):
    count = len(s)

    if count == 0:
        return 'Nobody likes it'
    if count == 1:
        return '{0[0]} likes it'.format(s)
    elif count == 2:
        return '{0[0]} and {0[1]} like it'.format(s)
    elif count == 3:
        return '{0[0]}, {0[1]} and {0[2]} like it'.format(s)
    else:
        return '{0[0]} and {count} other people liked it'.format(s)

print(insta(s))