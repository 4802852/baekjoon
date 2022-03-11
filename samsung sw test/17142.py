import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

from collections import deque

rc = [0, 1, 0, -1]
cc = [1, 0, -1, 0]
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
empty = 0
virus = []
for r in range(N):
    for c in range(N):
        if matrix[r][c] == 0:
            empty += 1
        elif matrix[r][c] == 2:
            virus.append((0, r, c))
ans = []


def count(virus_list, empty_space):
    # bfs 알고리즘을 이용하여 바이러스가 퍼지는 시간을 계산하는 함수
    queue = deque(virus_list)
    visited = [[0] * N for _ in range(N)]
    for t, r, c in virus_list:
        visited[r][c] = 1
    max_t = 0
    while queue:
        t, r, c = queue.popleft()
        if matrix[r][c] == 0:
            # 비활성화 바이러스에서의 시간은 카운트하지 않는다.
            max_t = max(max_t, t)
        for i in range(4):
            nr, nc = r + rc[i], c + cc[i]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and matrix[nr][nc] != 1:
                if matrix[nr][nc] == 0:
                    # (nr, nc) 위치가 빈공간일 경우에만 카운트 해준다.
                    empty_space -= 1
                visited[nr][nc] = 1
                queue.append((t + 1, nr, nc))
    if empty_space:
        # 계산이 완료되었을 때 빈 공간이 남아있다면 -1 리턴
        return -1
    else:
        # 빈 공간이 남아있지 않다면 최대 시간 리턴
        return max_t


def dfs(depth, last_val, selected):
    # dfs 알고리즘 이용하여 조합(Combination) 구현
    if len(selected) == M:
        # M 개의 바이러스가 모두 선택되었을 경우 바이러스가 퍼지는 시간 계산
        tmp_virus = []
        for n in selected:
            tmp_virus.append(virus[n])
        res = count(tmp_virus, empty)
        if res != -1:
            ans.append(res)
        return
    for i in range(last_val + 1, len(virus) - M + 1 + depth):
        selected.append(i)
        dfs(depth + 1, i, selected)
        selected.remove(i)


dfs(0, -1, [])
if ans:
    print(min(ans))
else:
    print(-1)
