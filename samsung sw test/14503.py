import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

N, M = map(int, input().split())
r, c, d = map(int, input().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))
rc = [-1, 0, 1, 0]
cc = [0, 1, 0, -1]


def clean(r, c, d, cnt):
    # 현재 위치가 청소되어있지 않다면 청소
    if matrix[r][c] == 0:
        cnt += 1
        matrix[r][c] = 2
    for i in range(1, 5):
        # 현재 방향을 기준으로 왼쪽 방향 순서대로 탐색하여 청소되지 않은 공간이 있을 경우 이동
        di = (d - i) % 4
        nr, nc = r + rc[di], c + cc[di]
        if matrix[nr][nc] == 0:
            return 1, cnt, nr, nc, di
    # 4방향 모두 청소가 완료되었을 경우, 새로 이동하는 위치는 후진
    nr, nc = r + rc[(d + 2) % 4], c + cc[(d + 2) % 4]
    if matrix[nr][nc] == 1:
        # 후진 시, 뒤가 벽일 경우 작동 중지를 뜻하는 0 리턴
        return 0, cnt, r, c, d
    else:
        # 후진 시, 뒤가 벽이 아닐 경우 후진한 위치 및 방향을 리턴
        return 1, cnt, nr, nc, d


flag = 1
cnt = 0
while flag:
    # clean 함수에서 작동 중지를 뜻하는 flag = 0 이 리턴될 때 까지 계속 반복
    flag, cnt, r, c, d = clean(r, c, d, cnt)
print(cnt)
