from msilib.schema import Error


class Reader:
    __books = []

    def __init__(self, name):
        self.name = name
    
    def get_book(self, name_of_book):
        if len(self.__books) > 2:
            return 'Error. Список переполнен'
        else:
            self.__books.append(name_of_book)
            print('Добавляю книгу в список')

    def give_book(self, name_of_book):
        if name_of_book in self.__books:
            self.__books.remove(name_of_book)
            print('Удаляю книгу из списка')
        else:
            return 'Error. Такой книги нет'

book1 = 'First'
book2 = 'Second'
