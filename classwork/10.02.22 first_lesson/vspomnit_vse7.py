N = int(input())

def generate(N):
    for i in range (0, N+1, 2):
        yield i

generate(N)