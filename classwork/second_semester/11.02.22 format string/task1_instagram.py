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
        return f'{s[0]} likes it'
    elif count == 2:
        return f'{s[0]} and {s[1]} like it'
    elif count == 3:
        return f'{s[0]}, {s[1]} and {s[2]} like it'
    else:
        return f'{s[0]} and {count-1} other people liked it'
