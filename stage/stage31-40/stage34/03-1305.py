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


l = int(sys.stdin.readline())
n = sys.stdin.readline().rstrip()

print(l - kmptable(n)[-1])