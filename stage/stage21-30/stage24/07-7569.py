import sys
from collections import deque

n, m, h = map(int, sys.stdin.readline().split())
tomato = [[list(map(int, sys.stdin.readline().split())) for _ in range(m)] for __ in range(h)]
q = deque([])
for i in range(h):
    for j in range(m):
        for k in range(n):
            if tomato[i][j][k] == 1:
                q.append([i, j, k])
dx = [1, 0, -1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


def bfs():
    while q:
        now = q.popleft()
        for i in range(6):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]
            nz = now[2] + dz[i]
            if 0 <= nx < h and 0 <= ny < m and 0 <= nz < n and tomato[nx][ny][nz] == 0:
                tomato[nx][ny][nz] = tomato[now[0]][now[1]][now[2]] + 1
                q.append([nx, ny, nz])


bfs()
maximum = 0
all = True
for i in tomato:
    for j in i:
        for k in j:
            if k > maximum:
                maximum = k
            if k == 0:
                all = False
if all:
    print(maximum - 1)
else:
    print(-1)