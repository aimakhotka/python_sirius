class Counter():
    __current = 0
    def __init__(self):
        self.__current = 0

    def __add(self):
        self.__current += 1
    
    def to_zero(self):
        self.__current = 0

    def get_current(self):
        return self.__current


c = Counter()
print(c._Counter__current)
c._Counter__add()
print(c._Counter__current)


