n = [1, 14, 6, 4, 9, 2, 4, 7]

def unique(n):
    list = []
    unique_n = set(n)

    for i in unique_n:
        list.append(i)
    
    return list

print (unique(n))