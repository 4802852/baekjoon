import sys
sys.setrecursionlimit(10 ** 6)


def dfs(x, visited, stack):
    visited[x] = 1
    for ne in graph[x]:
        if visited[ne] == 0:
            dfs(ne, visited, stack)
    stack.append(x)


def reverse_dfs(x, visited, scc):
    global idid
    visited[x] = 1
    ids[x] = idid
    scc.append(x)
    for ne in reverse_graph[x]:
        if visited[ne] == 0:
            reverse_dfs(ne, visited, scc)


t = int(sys.stdin.readline())
while t:
    income = sys.stdin.readline()
    if income == '\n':
        continue
    n, m = map(int, income.split())
    graph = [[] for _ in range(n)]
    reverse_graph = [[] for _ in range(n)]
    for __ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        reverse_graph[b].append(a)
    stack = []
    visited = [0] * n
    for i in range(n):
        if visited[i] == 0:
            dfs(i, visited, stack)
    idid = -1
    ids = [-1] * n
    visited = [0] * n
    result = [[] for __ in range(n)]
    while stack:
        scc = []
        node = stack.pop()
        if visited[node] == 0:
            idid += 1
            reverse_dfs(node, visited, scc)
            result[idid] = scc
    scc_indegree = [0] * (idid + 1)
    for i in range(n):
        for to in graph[i]:
            if ids[i] != ids[to]:
                scc_indegree[ids[to]] += 1
    tmp = []
    cnt = 0
    for i in range(len(scc_indegree)):
        if scc_indegree[i] == 0:
            for j in result[i]:
                tmp.append(j)
            cnt += 1
    if cnt == 1:
        for i in sorted(tmp):
            print(i)
    else:
        print("Confused")
    print()
    t -= 1
