import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

N, M = map(int, input().split())
B = []
max_val = 0
for i in range(N):
    B.append(list(map(int, input().split())))
    max_val = max(max_val, max(B[i]))
visited = [[0] * M for _ in range(N)]
ans = 0
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def dfs(r, c, depth, sum):
    global max_val, ans
    if ans >= sum + max_val * (4 - depth):
        return
    if depth == 4:
        ans = max(ans, sum)
        return
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0:
            if depth == 2:
                visited[nr][nc] = 1
                dfs(r, c, depth + 1, sum + B[nr][nc])
                visited[nr][nc] = 0
            visited[nr][nc] = 1
            dfs(nr, nc, depth + 1, sum + B[nr][nc])
            visited[nr][nc] = 0


for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i, j, 1, B[i][j])
        visited[i][j] = 0

print(ans)
