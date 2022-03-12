import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

N = int(input())
matrix = []
sum_val = 0
for i in range(N):
    tmp = list(map(int, input().split()))
    sum_val += sum(tmp)
    matrix.append(tmp)


def count(x, y, d1, d2, sum_val):
    # 각 구역의 인구수를 카운트하여 5 구역 간 최대 인구수 차이를 리턴하는 함수
    population = [0] * 5
    # r, lc, rc : r 행에서 5구역을 구분하는 가장 왼쪽값 lc 와 가장 오른쪽 값 rc
    r, lc, rc = 0, y, y + 1
    while r < N:
        if r < x:
            # 5구역에 도달하기 전 r 행에서 1구역과 2구역에 해당하는 인구수 계산
            population[0] += sum(matrix[r][: (y + 1)])
            population[1] += sum(matrix[r][(y + 1) :])
        elif x + d1 + d2 < r:
            # 5구역을 지나친 후 r 행에서 3구역과 4구역에 해당하는 인구수 계산
            population[2] += sum(matrix[r][: (y + d2 - d1)])
            population[3] += sum(matrix[r][(y + d2 - d1) :])
        else:
            # 5구역이 존재하는 r 행에서
            # lc 는 x + d1 행 전까지 1구역, 이후에는 3구역
            if r < x + d1:
                population[0] += sum(matrix[r][:lc])
                lc -= 1
            else:
                population[2] += sum(matrix[r][:lc])
                lc += 1
            # rc 는 x + d2 행까지 2구역, 이후에는 4구역
            if r < x + d2:
                population[1] += sum(matrix[r][rc:])
                rc += 1
            elif r == x + d2:
                population[1] += sum(matrix[r][rc:])
                rc -= 1
            else:
                population[3] += sum(matrix[r][rc:])
                rc -= 1
        r += 1
    #전체 인구에서 1,2,3,4 구역 합을 빼주어 5구역 인구수를 계산
    population[4] = sum_val - sum(population[:4])
    return max(population) - min(population)


ans = []
for d2 in range(1, N - 2):
    for d1 in range(1, N - d2):
        for c in range(d1, N - d2):
            for r in range(0, N - d1 - d2):
                ans.append(count(r, c, d1, d2, sum_val))
print(min(ans))
