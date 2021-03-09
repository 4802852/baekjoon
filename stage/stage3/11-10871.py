import sys

n, x = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
b = []
for i in range(n):
    if a[i] < x:
        b.append(a[i])
print(' '.join(map(str, b)))