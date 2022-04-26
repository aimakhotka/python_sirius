import phonenumbers

my_number = input()
true_number = phonenumbers.parse(my_number)
print(phonenumbers.is_valid_number(true_number))
