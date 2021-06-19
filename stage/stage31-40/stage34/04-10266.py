import sys


def kmptable(a):
    m = len(a)
    table = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and a[i] != a[j]:
            j = table[j - 1]
        if a[i] == a[j]:
            j += 1
            table[i] = j
    return table


def kmp(s, p):
    table = kmptable(p)
    j = 0
    for i in range(len(s)):
        while j > 0 and s[i] != p[j]:
            j = table[j - 1]
        if s[i] == p[j]:
            if j == len(p) - 1:
                return True
            else:
                j += 1
    return False


n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

clock1 = [0] * 360000
clock2 = [0] * 360000

for i in a:
    clock1[i] = 1
for i in b:
    clock2[i] = 1

clock1 += clock1

if kmp(clock1, clock2):
    print("possible")
else:
    print("impossible")
