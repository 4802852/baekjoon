import sys

dx = [2, 2, 1, 1, -1, -1, -2, -2]
dy = [1, -1, 2, -2, 2, -2, 1, -1]


def bfs():
    visited = [[-1] * n for __ in range(n)]
    q = []
    q.append(start)
    visited[start[0]][start[1]] = 0
    while q:
        now = q.pop(0)
        if now == end:
            return visited[now[0]][now[1]]
        for i in range(8):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                visited[nx][ny] = visited[now[0]][now[1]] + 1
                q.append([nx, ny])


for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    start = list(map(int, sys.stdin.readline().split()))
    end = list(map(int, sys.stdin.readline().split()))
    print(bfs())
