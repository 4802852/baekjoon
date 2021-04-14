import sys


def bfs(a):
    q.append(a)
    visited[a] = 1
    while q:
        now = q.pop(0)
        for i in range(len(lines[now])):
            if visited[lines[now][i]] == 0:
                visited[lines[now][i]] = -1 * visited[now]
                q.append(lines[now][i])
            if visited[lines[now][i]] == visited[now]:
                return 0
    return 1


for _ in range(int(sys.stdin.readline())):
    v, e = map(int, sys.stdin.readline().split())
    lines = [[] for _ in range(v + 1)]
    for _ in range(e):
        x, y = map(int, sys.stdin.readline().split())
        lines[x].append(y)
        lines[y].append(x)
    visited = [0 for _ in range(v + 1)]
    q = []
    ans = 1
    for i in range(v):
        if visited[i] == 0:
            ans = bfs(i)
            if ans == 0:
                break
    if ans == 1:
        print('YES')
    else:
        print('NO')