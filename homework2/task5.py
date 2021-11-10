n = [1, 7, 4, 2, 4, 6, 8, 3, 0, 7]

def unique(n):
    list = []
    unique_n = set(n)

    for i in unique_n:
        list.append(i)
    
    return list

print (unique(n))