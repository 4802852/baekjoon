import sys

sys.setrecursionlimit(10 ** 9)
n = int(sys.stdin.readline())
population = [0] + list(map(int, sys.stdin.readline().split()))
lines = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    lines[a].append(b)
    lines[b].append(a)
visited = [0] * (n + 1)
dp = [[0, 0] for _ in range(n + 1)]


def dfs(start):
    visited[start] = 1
    dp[start][0] = population[start]
    for i in lines[start]:
        if not visited[i]:
            dfs(i)
            dp[start][0] += dp[i][1]
            dp[start][1] += max(dp[i][1], dp[i][0])


dfs(1)
print(max(dp[1][0], dp[1][1]))