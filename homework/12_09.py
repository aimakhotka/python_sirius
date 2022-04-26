from random import randint
 
n = 10
a = []
for i in range(n):
    a.append(randint(0, 1000))
print(a)
 
for i in range(n-1):
    for k in range(n-i-1):
        if a[k] > a[k+1]:
            a[k], a[k+1] = a[k+1], a[k]
 
print(a)