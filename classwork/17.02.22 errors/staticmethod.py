from lib2to3.pgen2.token import DOUBLESLASH


class A:
    @staticmethod
    def new_method():
        pass # наша логика

class Phone:
    @staticmethod
    def country(num):
        return num[1:-14]

    def check_num(num):
        formated_num = num[1:].split('-')
        string_num = ''.join(formated_num)
        dash = num[-3] == num[-6] == num[-10] == num[-14] == '-'
        return string_num.isdigit() and dash

my_num = '7-922-664-82-5'
print(Phone.check_num(my_num))