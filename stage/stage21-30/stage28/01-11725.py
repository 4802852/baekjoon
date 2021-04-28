import sys

n = int(sys.stdin.readline())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)
parent = [0 for _ in range(n + 1)]
q = [1]
while q:
    now = q.pop(0)
    for i in tree[now]:
        if parent[i] == 0:
            parent[i] = now
            q.append(i)
for i in parent[2:]:
    print(i)