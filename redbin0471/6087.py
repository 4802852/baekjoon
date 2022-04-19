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


def bfs(sr, sc, er, ec):
    visited = [[-1] * C for _ in range(R)]
    queue = deque()
    visited[sr][sc] = 0
    queue.append((sr, sc))
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            while 1:
                if (
                    # 배열 바깥으로 나가거나
                    nr < 0
                    or R <= nr
                    or nc < 0
                    or C <= nc
                    # 벽을 만나거나
                    or matrix[nr][nc] == "*"
                    # 다음 위치가 이미 방문되었는데, 현재 탐색중인 거울 수보다 작은 횟수로 이동 가능할 경우
                    or 0 < visited[nr][nc] < visited[r][c] + 1
                ):
                    # 해당 방향 탐색 종료
                    break
                # 위치를 큐에 추가하고
                queue.append((nr, nc))
                # visited[nr][nc] 를 visited[r][c] + 1 로 저장함으로써, (r, c)에서 출발하여 네 방향에 있는 모든 미방문 점은 같은 수를 가지게 된다.
                visited[nr][nc] = visited[r][c] + 1
                nr, nc = nr + dr[i], nc + dc[i]
    # 처음 시작 위치가 0으로 시작하여, 0회로 도달할 수 있는 곳을 1로 저장했기 때문에 마지막에 1을 뺀 값을 출력해준다.
    return visited[er][ec] - 1


C, R = map(int, input().split())
matrix = [list(input().strip()) for _ in range(R)]
cs = []
for i in range(R):
    for j in range(C):
        if matrix[i][j] == "C":
            cs += [i, j]
            matrix[i][j] = "."
ans = bfs(cs[0], cs[1], cs[2], cs[3])
print(ans)
