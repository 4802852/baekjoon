import sys

INF = float('inf')
n, m = map(int, sys.stdin.readline().split())
lines = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
bf = [INF] * (n + 1)


def solve_bf():
    bf[1] = 0
    minus = False
    for i in range(n):
        for j in range(m):
            v = lines[j][0]
            nv = lines[j][1]
            w = lines[j][2]
            if bf[v] != INF and bf[nv] > bf[v] + w:
                bf[nv] = bf[v] + w
                if i == n - 1:
                    minus = True
    if minus:
        print(-1)
    else:
        for k in range(2, n + 1):
            if bf[k] == INF:
                print(-1)
            else:
                print(bf[k])


solve_bf()