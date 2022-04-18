import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

import sys
from collections import deque

input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


# (r, c)에서 시작하여 진행하면서 해당 위치에 도달하기 까지 문을 연 갯수를 해당 칸에 표시
def bfs(r, c):
    visited = [[-1] * (C + 2) for _ in range(R + 2)]
    queue = deque()
    queue.append((r, c))
    visited[r][c] = 0
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if nr < 0 or R + 2 <= nr or nc < 0 or C + 2 <= nc or visited[nr][nc] != -1:
                continue
            if matrix[nr][nc] == ".":
                # 문을 열지 않았다면 appendleft 해줌으로써 가중치가 작은(문을 덜 여는) 경로가 우선적으로 탐색될 수 있도록 함
                visited[nr][nc] = visited[r][c]
                queue.appendleft((nr, nc))
            elif matrix[nr][nc] == "#":
                # 문을 열었다면 문 연 갯수를 1 더해주고 큐의 맨 뒤로 추가
                visited[nr][nc] = visited[r][c] + 1
                queue.append((nr, nc))
    return visited


T = int(input())
for _ in range(T):
    R, C = map(int, input().split())
    matrix = ["." * (C + 2)]
    for _ in range(R):
        matrix.append(["."] + list(input().strip()) + ["."])
    matrix.append(["."] * (C + 2))
    prisoner = []
    for i in range(R + 2):
        for j in range(C + 2):
            if matrix[i][j] == "$":
                prisoner.append([i, j])
                matrix[i][j] = "."

    cnt1 = bfs(prisoner[0][0], prisoner[0][1])
    cnt2 = bfs(prisoner[1][0], prisoner[1][1])
    cnt3 = bfs(0, 0)
    
    ans = float("inf")
    for i in range(1, R + 1):
        for j in range(1, C + 1):
            if cnt1[i][j] == -1 or cnt2[i][j] == -1 or cnt3[i][j] == -1:
                continue
            if matrix[i][j] == ".":
                ans = min(ans, cnt1[i][j] + cnt2[i][j] + cnt3[i][j])
            elif matrix[i][j] == "#":
                ans = min(ans, cnt1[i][j] + cnt2[i][j] + cnt3[i][j] - 2)
    print(ans)
