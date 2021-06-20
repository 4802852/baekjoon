import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
q = deque()
graph_list = []
student_list = [[] for _ in range(n + 1)]
in_degree = [0 for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    in_degree[b] += 1
    student_list[a].append(b)

for i in range(1, n + 1):
    if in_degree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    print(now, end=" ")
    for d in student_list[now]:
        in_degree[d] -= 1
        if in_degree[d] == 0:
            q.append(d)