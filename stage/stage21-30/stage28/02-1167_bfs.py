from collections import deque
import sys

n = int(sys.stdin.readline())
tree = [[] for _ in range(n + 1)]
for _ in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    i = 1
    while i != len(tmp) - 1:
        tree[tmp[0]].append([tmp[i], tmp[i + 1]])
        i += 2


def bfs(start):
    queue = deque()
    queue.append([start, 0])
    visited = [0 for _ in range(n + 1)]
    maxd = 0
    maxi = start
    visited[start] = 1
    while queue:
        nowi, nowd = queue.popleft()
        if maxd < nowd:
            maxd = nowd
            maxi = nowi
        for e, d in tree[nowi]:
            if visited[e] == 0:
                queue.append([e, nowd + d])
                visited[e] = 1
    return maxi, maxd


tmpindex, tmpmax = bfs(1)
finalindex, finalmax = bfs(tmpindex)
print(finalmax)
