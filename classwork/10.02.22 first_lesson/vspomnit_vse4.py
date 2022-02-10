def func(stroka, spisok):
    new_str = ''

    for i in spisok:
        if i >= 0 and i < len(stroka):
            new_str += stroka[i]
    return new_str