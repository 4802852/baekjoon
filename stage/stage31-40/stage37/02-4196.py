import sys
sys.setrecursionlimit(10 ** 6)


def dfs(x, low, ids, visited, stack):
    global idid
    ids[x] = idid
    low[x] = idid
    idid += 1
    visited[x] = 1
    stack.append(x)
    for ne in graph[x]:
        if ids[ne] == -1:
            dfs(ne, low, ids, visited, stack)
            low[x] = min(low[x], low[ne])
        elif visited[ne] == 1:
            low[x] = min(low[x], ids[ne])
    w = -1
    scc = []
    if low[x] == ids[x]:
        while w != x:
            w = stack.pop()
            scc.append(w)
            visited[w] = -1
        result.append(sorted(scc))


t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    graph = [[] for ___ in range(n + 1)]
    indegree = [0] * (n + 1)
    for __ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        indegree[b] += 1
    cnt = 0
    stack = []
    idid = 0
    result = []
    ids = [-1] * (n + 1)
    low = [-1] * (n + 1)
    visited = [0] * (n + 1)
    for i in range(1, n + 1):
        if ids[i] == -1:
            dfs(i, low, ids, visited, stack)
    for scc in result:
        if len(scc) == 1:
            if indegree[scc[0]] == 0:
                cnt += 1
        else:
            tmp = True
            for j in scc:
                if indegree[j] > 1:
                    tmp = False
            if tmp:
                cnt += 1
    print(cnt)