import sys


def kmptable(a):
    n = len(a)
    table = [0] * n
    j = 0
    for i in range(1, n):
        while j > 0 and a[i] != a[j]:
            j = table[j - 1]
        if a[i] == a[j]:
            j += 1
            table[i] = j
    return table


while 1:
    p = sys.stdin.readline().rstrip()
    if p == '.':
        break
    table = kmptable(p)
    mod = len(p) - table[-1]
    if len(p) % mod == 0:
        print(len(p) // mod)
    else:
        print(1)
