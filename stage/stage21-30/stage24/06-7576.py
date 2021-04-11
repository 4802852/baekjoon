import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
tomato = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
q = deque([])
for i in range(m):
    for j in range(n):
        if tomato[i][j] == 1:
            q.append([i, j])
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
while q:
    now = q.popleft()
    for i in range(4):
        nx = now[0] + dx[i]
        ny = now[1] + dy[i]
        if 0 <= nx < m and 0 <= ny < n and tomato[nx][ny] == 0:
            tomato[nx][ny] = tomato[now[0]][now[1]] + 1
            q.append([nx, ny])
maximum = 0
all = True
for i in tomato:
    for j in i:
        if j > maximum:
            maximum = j
        if j == 0:
            all = False
if all:
    print(maximum - 1)
else:
    print(-1)