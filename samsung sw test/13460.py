import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

from collections import deque

# 구슬의 이동 방향
rc = [1, 0, -1, 0]
cc = [0, 1, 0, -1]


# 구슬의 위치 및 이동 방향을 입력 받아 이동 위치 및 이동 거리를 리턴하는 함수
def move(r, c, di):
    cnt = 0
    while matrix[r + rc[di]][c + cc[di]] != "#" and matrix[r][c] != "O":
        r += rc[di]
        c += cc[di]
        cnt += 1
    return r, c, cnt


# 두 구슬의 위치를 입력 받아 BFS 알고리즘을 이용하여 문제를 해결하는 함수
def solve(rr, cr, rb, cb):
    queue = deque([])
    # 처음 위치를 queue에 추가하고, visited 표시
    queue.append((rr, cr, rb, cb, 1))
    visited[rr][cr][rb][cb] = True
    while queue:
        rr, cr, rb, cb, depth = queue.popleft()
        # 10번 이내에 목적지에 도달하지 못할 경우 실패
        if depth > 10:
            break
        for di in range(4):
            # 4 방향으로 각 구슬 이동
            nrr, ncr, rcnt = move(rr, cr, di)
            nrb, ncb, bcnt = move(rb, cb, di)
            if matrix[nrb][ncb] != "O":
                if matrix[nrr][ncr] == "O":
                    # 빨간 구슬이 목적한 위치(구멍)에 도달할 경우 depth(횟수) 리턴
                    return depth
                if nrr == nrb and ncr == ncb:
                    # 빨간 구슬과 파란 구슬이 같은 위치에 위치할 경우, 이동거리가 더 짧은 쪽을 한칸 복귀
                    if rcnt > bcnt:
                        nrr -= rc[di]
                        ncr -= cc[di]
                    else:
                        nrb -= rc[di]
                        ncb -= cc[di]
                if not visited[nrr][ncr][nrb][ncb]:
                    # 이동된 위치가 visited 되지 않았을 경우 visited 표시하고, queue에 추가
                    visited[nrr][ncr][nrb][ncb] = True
                    queue.append((nrr, ncr, nrb, ncb, depth + 1))
    return -1


N, M = map(int, input().split())
matrix = [[""] * M for _ in range(N)]
for i in range(N):
    line_tmp = list(input())
    for j in range(M):
        if line_tmp[j] == "R":
            rr, cr = i, j
        if line_tmp[j] == "B":
            rb, cb = i, j
        matrix[i][j] = line_tmp[j]
visited = [[[[False] * M for _ in range(N)] for __ in range(M)] for ___ in range(N)]
res = solve(rr, cr, rb, cb)
print(res)
