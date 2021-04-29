import sys


def bfs(x):
    isTree = True
    q = [x]
    while q:
        now = q.pop(0)
        if visited[now] == 1:
            isTree = False
        visited[now] = 1
        for j in graph[now]:
            if visited[j] == 0:
                q.append(j)
    return isTree


case = 0
while True:
    case += 1
    n, m = map(int, sys.stdin.readline().split())
    if [n, m] == [0, 0]:
        break
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    treeCnt = 0
    visited = [0] * (n + 1)
    for i in range(1, n + 1):
        if visited[i] == 1:
            continue
        if bfs(i) is True:
            treeCnt += 1
    if treeCnt == 0:
        print('Case {}: No trees.'.format(case))
    elif treeCnt == 1:
        print('Case {}: There is one tree.'.format(case))
    else:
        print('Case {}: A forest of {} trees.'.format(case, treeCnt))