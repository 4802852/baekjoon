import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
lines = [[0 for _ in range(n + 1)] for __ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    lines[a][b] = lines[b][a] = 1
visited = [0 for _ in range(n + 1)]


def dfs(x):
    visited[x] = 1
    for i in range(1, n + 1):
        if visited[i] == 0 and lines[x][i] == 1:
            dfs(i)


dfs(1)
print(sum(visited) - 1)