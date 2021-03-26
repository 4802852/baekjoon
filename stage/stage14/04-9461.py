import sys


p = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
n = int(sys.stdin.readline())
for i in range(n):
    m = int(sys.stdin.readline())
    if m < len(p):
        print(p[m])
    else:
        for i in range(len(p), m + 1):
            p.append(p[-1] + p[-5])
        print(p[-1])