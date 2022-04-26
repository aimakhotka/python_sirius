class OddNumberError(Exception):
    pass

try:
    for i in range(0, 10):
        if i % 2 != 0:
            raise OddNumberError
        print(i)
    
except Exception:
    print('Ошибка!')