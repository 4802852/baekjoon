import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]


def count(x, y, d1, d2):
    # 각 구역의 인구수를 카운트하여 5 구역 간 최대 인구수 차이를 리턴하는 함수
    population = [0] * 5
    for r in range(N):
        for c in range(N):
            if x + y <= r + c <= x + y + 2 * d2 and x - y <= r - c <= x - y + 2 * d1:
                # 5구역에 해당하는 조건
                population[4] += matrix[r][c]
            elif 0 <= r < x + d1 and 0 <= c <= y:
                # 1구역에 해당하는 조건... 이하 생략
                population[0] += matrix[r][c]
            elif 0 <= r <= x + d2 and y < c < N:
                population[1] += matrix[r][c]
            elif x + d1 <= r < N and 0 <= c < y - d1 + d2:
                population[2] += matrix[r][c]
            elif x + d2 < r < N and y - d1 + d2 <= c < N:
                population[3] += matrix[r][c]
    # population 함수의 max 값과 min 값의 차이를 리턴
    return max(population) - min(population)


ans = []
for r in range(0, N - 2):
    for c in range(1, N - 1):
        for d1 in range(1, N - 1):
            for d2 in range(1, N - 1):
                if N <= r + d1 + d2 or c - d1 < 0 or N < c + d2:
                    # 값이 행렬을 벗어나는 경우 생략
                    continue
                ans.append(count(r, c, d1, d2))
print(min(ans))
