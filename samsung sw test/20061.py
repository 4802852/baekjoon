import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

N = int(input())
green_blue = [[[0] * 4 for _ in range(6)] for __ in range(2)]


def rain(t, x, y):
    for n in range(2):
        if n == 1:
            # blue 박스(n = 1) 일 경우 좌표를 변환해준다.
            if t == 2:
                t = 3
            elif t == 3:
                t = 2
            x, y = y, 3 - x
        i = 0
        while i < 6:
            # 마지막 위치이거나, 다음칸에 블록이 있을 경우 블록을 위치시킨다.
            if (t == 1 or t == 3) and (i == 5 or green_blue[n][i + 1][y] == 1):
                green_blue[n][i][y] = 1
                if t == 3:
                    green_blue[n][i - 1][y] = 1
                break
            elif t == 2 and (
                i == 5
                or (
                    green_blue[n][i + 1][y] == 1
                    or green_blue[n][i + 1][y + 1 if n == 0 else y - 1] == 1
                )
            ):
                green_blue[n][i][y] = 1
                green_blue[n][i][y + 1 if n == 0 else y - 1] = 1
                break
            i += 1


def rearrange(prev_score):
    sum_val = [0, 0, prev_score]
    for n in range(2):
        i = 5
        while 2 <= i:
            # 연한 색의 특별한 칸에 도달하기 전까지
            if sum(green_blue[n][i]) == 4:
                # 칸이 모두 채워져있으면 해당 칸을 삭제하고 점수를 1점 획득한다.
                del green_blue[n][i]
                green_blue[n] = [[0] * 4] + green_blue[n]
                sum_val[2] += 1
            else:
                # 채워져있지 않을 경우 블록 수를 카운트해준다.
                sum_val[n] += sum(green_blue[n][i])
                i -= 1
        while 0 <= i:
            # 연한 색의 특별한 칸에 도달할 경우
            if sum(green_blue[n][i]):
                # 특별한 칸에 블록이 있을 경우 맨 아래칸을 삭제하고 맨위에 빈칸을 추가한다.
                sum_val[n] -= sum(green_blue[n][-1])
                sum_val[n] += sum(green_blue[n][i])
                green_blue[n] = [[0] * 4] + green_blue[n][:-1]
            else:
                i -= 1
    return sum_val


ans = [0, 0, 0]
for _ in range(N):
    t, x, y = map(int, input().split())
    rain(t, x, y)
    ans = rearrange(ans[2])
print(ans[2])
print(ans[1] + ans[0])
