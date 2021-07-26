import sys
sys.setrecursionlimit(10 ** 6)


def dfs(x, low, ids, visited, stack):
    global idid, graph, result
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
        result.append(scc)


def find_scc():
    global idid, result
    stack = []
    low = [-1] * ((n + 1) * 2)
    ids = [-1] * ((n + 1) * 2)
    visited = [0] * ((n + 1) * 2)
    idid = 0
    result = []

    for i in range(1, (n + 1) * 2):
        if ids[i] == -1:
            dfs(i, low, ids, visited, stack)


def main():
    global n, graph
    n, m = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range((n + 1) * 2)]
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        if a < 0:
            a = (-a) * 2 + 1
            not_a = a - 1
        else:
            a = a * 2
            not_a = a + 1
        if b < 0:
            b = (-b) * 2 + 1
            not_b = b - 1
        else:
            b = b * 2
            not_b = b + 1
        graph[not_a].append(b)
        graph[not_b].append(a)
    find_scc()
    ans = 1
    for i in result:
        if len(i) > 1:
            ans = 0
    print(ans)


main()
