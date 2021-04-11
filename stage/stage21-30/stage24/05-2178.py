import sys


def bfs(x, y):
    global cnt
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    q = [[x, y]]
    visited[x][y] = 1
    while q:
        now = q.pop(0)
        for i in range(4):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1 and visited[nx][ny] == 0:
                q.append([nx, ny])
                visited[nx][ny] = visited[now[0]][now[1]] + 1


n, m = map(int, sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
visited = [[0 for _ in range(m)] for __ in range(n)]
bfs(0, 0)
print(visited[n - 1][m - 1])
