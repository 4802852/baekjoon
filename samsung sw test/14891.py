import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

gear = [list(map(int, input())) for _ in range(4)]


def rotate(n, d):
    if d == 1:
        tmp = gear[n][-1]
        for i in range(7, 0, -1):
            gear[n][i] = gear[n][i - 1]
        gear[n][0] = tmp
    elif d == -1:
        tmp = gear[n][0]
        for i in range(7):
            gear[n][i] = gear[n][i + 1]
        gear[n][7] = tmp


def check(g, r):
    g -= 1
    rotate_list = [0, 0, 0, 0]
    rotate_list[g] = r
    for i in range(1, 4):
        if g + i < 4:
            if gear[g + i - 1][2] != gear[g + i][6]:
                rotate_list[g + i] = -1 * rotate_list[g + i - 1]
        if 0 <= g - i:
            if gear[g - i][2] != gear[g - i + 1][6]:
                rotate_list[g - i] = -1 * rotate_list[g - i + 1]
    for i in range(4):
        rotate(i, rotate_list[i])


K = int(input())
for _ in range(K):
    g, r = map(int, input().split())
    check(g, r)
ans = gear[0][0] + gear[1][0] * 2 + gear[2][0] * 4 + gear[3][0] * 8
print(ans)
