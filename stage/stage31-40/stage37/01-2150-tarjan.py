import sys
sys.setrecursionlimit(10 ** 6)

v, e = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

stack = []
low = [-1] * (v + 1)
ids = [-1] * (v + 1)
visited = [0] * (v + 1)
idid = 0
result = []


def dfs(x, low, ids, visited, stack, idid):
    idid += 1
    ids[x] = idid
    low[x] = idid
    visited[x] = 1
    stack.append(x)

    for ne in graph[x]:
        if ids[ne] == -1:
            dfs(ne, low, ids, visited, stack, idid)
            low[x] = min(low[x], low[ne])
        elif visited[ne] == 1:
            low[x] = min(low[x], ids[ne])

    w = -1
    scc = []
    if low[x] == ids[x]:
        while w != x:
            w = stack.pop()
            scc.append(w)
        result.append(sorted(scc))


for i in range(1, v + 1):
    if visited[i] == 0:
        dfs(i, low, ids, visited, stack, idid)
print(len(result))
for i in sorted(result):
    print(*i, -1)