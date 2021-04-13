import sys

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs():
    q = []
    q.append([0, 0, 1])
    visit = [[[0] * 2 for _ in range(m)] for __ in range(n)]
    visit[0][0][1] = 1
    while q:
        x, y, w = q.pop(0)
        if x == n - 1 and y == m - 1:
            return visit[x][y][w]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if location[nx][ny] == 1 and w == 1:
                    visit[nx][ny][0] = visit[x][y][1] + 1
                    q.append([nx, ny, 0])
                elif location[nx][ny] == 0 and visit[nx][ny][w] == 0:
                    visit[nx][ny][w] = visit[x][y][w] + 1
                    q.append([nx, ny, w])
    return -1


n, m = map(int, sys.stdin.readline().split())
location = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
print(bfs())