import sys

INF = float('inf')
n = int(sys.stdin.readline())
w = []
for _ in range(n):
    w.append(list(map(int, sys.stdin.readline().split())))
dp = [[-1] * (1 << n) for _ in range(n)]


def dfs(x, visited):
    if visited == (1 << (n - 1)) - 1:
        if w[x][0]:
            return w[x][0]
        else:
            return INF
    if dp[x][visited] != -1:
        return dp[x][visited]
    dp[x][visited] = INF
    for i in range(1, n):
        if not w[x][i]:
            continue
        if visited & (1 << i - 1):
            continue
        dp[x][visited] = min(dp[x][visited], dfs(i, visited | (1 << (i - 1))) + w[x][i])
    return dp[x][visited]


print(dfs(0, 0))
