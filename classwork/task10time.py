t = int(input())


def time(t):
    s1 = t // 86400 #дни
    t = t % 86400
    s2 = t // 3600 #часы
    t = t % 3600
    s3 = t // 60 #минуты
    t = t % 60 #секунды
    return (str(s1) + '.' + str(s2) + '.' + str(s3) + '.' + str(t) + '.')

print(time(t))




