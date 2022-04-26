spisok_input = []

def ordered(spisok_input):
    new_spisok = []

    for i in len(spisok_input):
        if not i in new_spisok:
            new_spisok.append(i)
    return new_spisok


# второе решение

def ordered2(spisok_input):
    return list(set(spisok_input))

