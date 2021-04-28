import sys

INF = float('inf')
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
dp = [[INF] * (n + 1) for _ in range(n + 1)]
prev = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if dp[a][b] > c:
        dp[a][b] = c
        prev[a][b] = a

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j and dp[i][j] > dp[i][k] + dp[k][j]:
                dp[i][j] = dp[i][k] + dp[k][j]
                prev[i][j] = prev[k][j]

for i in dp[1:]:
    tmp = []
    for j in i[1:]:
        if j == INF:
            tmp.append(0)
        else:
            tmp.append(j)
    print(*tmp)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if dp[i][j] == INF:
            print(0)
        else:
            route = [j]
            tmp = j
            while tmp != i:
                route.append(prev[i][tmp])
                tmp = prev[i][tmp]
            print(len(route), end=' ')
            print(*route[::-1])
