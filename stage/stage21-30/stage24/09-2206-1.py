import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs():
    q = deque()
    q.append([0, 0, 0])
    visit = [[[float("inf")] * 2 for _ in range(m)] for __ in range(n)]
    visit[0][0][0] = 1
    while q:
        x, y, w = q.popleft()
        if x == n - 1 and y == m - 1:
            return visit[x][y][w]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if location[nx][ny] == 0 and visit[x][y][w] + 1 < visit[nx][ny][w]:
                    visit[nx][ny][w] = visit[x][y][w] + 1
                    q.append([nx, ny, w])
                elif (
                    location[nx][ny] == 1
                    and w < 1
                    and visit[x][y][w] + 1 < visit[nx][ny][w + 1]
                ):
                    visit[nx][ny][w + 1] = visit[x][y][w] + 1
                    q.append([nx, ny, w + 1])
    return -1


n, m = map(int, sys.stdin.readline().split())
location = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
print(bfs())
