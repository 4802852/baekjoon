import sys

INF = float('inf')
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
s = [[INF] * (n + 1) for i in range(n + 1)]

for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if s[a][b] > c:
        s[a][b] = c

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j and s[i][j] > s[i][k] + s[k][j]:
                s[i][j] = s[i][k] + s[k][j]

for i in s[1:]:
    for j in i[1:]:
        if j == INF:
            print(0, end=' ')
        else:
            print(j, end=' ')
    print()