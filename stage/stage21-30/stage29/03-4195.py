import sys


def find(x):
    if connect[x] == x:
        return x
    p = find(connect[x])
    connect[x] = p
    return p


def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        connect[y] = x
        number[x] += number[y]
    print(number[x])


for _ in range(int(sys.stdin.readline())):
    connect = dict()
    number = dict()
    for __ in range(int(sys.stdin.readline())):
        a, b = sys.stdin.readline().split()
        if a not in connect:
            connect[a] = a
            number[a] = 1
        if b not in connect:
            connect[b] = b
            number[b] = 1
        union(a, b)
