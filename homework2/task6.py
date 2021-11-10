def sort_1(list1):
    a = list1
    a.sort()
    return
def sort_2(list1):
    a = list1
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a
print(sort_1([1500, 123, 493, 82319, 38290193]))
print(sort_2([15, 343, 493, 19, 39343324]))