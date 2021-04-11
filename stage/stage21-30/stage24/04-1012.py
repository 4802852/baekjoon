import sys


def dfs(x, y):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    assigned[x][y] = cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and array[nx][ny] == 1 and assigned[nx][ny] == 0:
            dfs(nx, ny)


sys.setrecursionlimit(10**6)
t = int(sys.stdin.readline())
for ___ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    array = [[0 for _ in range(n)] for __ in range(m)]
    assigned = [[0 for _ in range(n)] for __ in range(m)]
    for _ in range(k):
        a, b = map(int, sys.stdin.readline().split())
        array[a][b] = 1
    cnt = 0
    for j in range(m):
        for k in range(n):
            if array[j][k] == 1 and assigned[j][k] == 0:
                cnt += 1
                dfs(j, k)
    print(cnt)
