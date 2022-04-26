from typing_extensions import ParamSpecKwargs


def sort_1(list1):
    a = list1
    a.sort()
    return a
def sort_2(list1):
    a = list1
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

print(sort_1([2, 5, 1, 200, 42, 4]))
print(sort_2([77, 23, 1, 6, 42, 10]))