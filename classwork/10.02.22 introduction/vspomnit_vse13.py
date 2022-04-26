def counter_of_letters(data):
    c_small = 0
    c_big = 0
    for i in data:
        if i.islower():
            c_small += 1
        if i.isupper():
            c_big += 1
    return c_small / len(data) * 100, c_big / len(data)*100