import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

import sys

input = sys.stdin.readline

N, H = map(int, input().split(" "))
down = [0] * (H + 1)
up = [0] * (H + 1)
min = N
num = 0

for i in range(N):
    if i % 2 == 0:
        down[int(input())] += 1
    else:
        up[int(input())] += 1
for i in range(H - 1, 0, -1):
    down[i] += down[i + 1]
    up[i] += up[i + 1]

for i in range(1, H + 1):
    if min > (down[i] + up[H - i + 1]):
        min = down[i] + up[H - i + 1]
        num = 1
    elif min == (down[i] + up[H - i + 1]):
        num += 1

print(min, num)
