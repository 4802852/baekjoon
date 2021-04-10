import sys

n, m, start = map(int, sys.stdin.readline().split())
lines = [[0 for _ in range(n + 1)] for __ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    lines[a][b] = lines[b][a] = 1
dfsvisited = [0 for _ in range(n + 1)]
bfsvisited = [0 for _ in range(n + 1)]
dfslist = []
bfslist = []


def dfs(x):
    dfsvisited[x] = 1
    dfslist.append(x)
    for i in range(1, n + 1):
        if dfsvisited[i] == 0 and lines[x][i] == 1:
            dfs(i)


def bfs(x):
    q = [x]
    bfsvisited[x] = 1
    while q:
        x = q.pop(0)
        bfslist.append(x)
        for i in range(1, n + 1):
            if bfsvisited[i] == 0 and lines[x][i] == 1:
                q.append(i)
                bfsvisited[i] = 1


dfs(start)
bfs(start)
print(*dfslist)
print(*bfslist)