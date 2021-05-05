import sys

sys.setrecursionlimit(10 ** 9)
n, r, q = map(int, sys.stdin.readline().split())
lines = [[] for _ in range(n + 1)]
subtree = [0] * (n + 1)
visited = [False] * (n + 1)
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    lines[a].append(b)
    lines[b].append(a)


def dfs(root):
    subtree[root] = 1
    visited[root] = True
    for i in lines[root]:
        if not visited[i]:
            dfs(i)
            subtree[root] += subtree[i]
    return


dfs(r)

for _ in range(q):
    print(subtree[int(sys.stdin.readline())])
