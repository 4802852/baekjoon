import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

N, L = map(int, input().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))


def solve(matrix):
    # 주어진 지도를 쪼개 경로 리스트로 만들어 지날 수 있는 길인지 판단하는 slope 함수에 전달
    cnt = 0
    for i in range(N):
        tmp = []
        for j in range(N):
            tmp.append(matrix[i][j])
        cnt += slope(tmp)
    for i in range(N):
        tmp = []
        for j in range(N):
            tmp.append(matrix[j][i])
        cnt += slope(tmp)
    return cnt


def slope(arr):
    sloped = [0] * N# 경사로가 놓아질 경우 표시할 리스트
    now = 0
    floor = arr[now]  # 현재 위치의 높이
    flag = 1  # 탐색 중 더이상 진행 불가능할 경우 flag = 0
    while flag:
        if now == len(arr) - 1:
            # 끝까지 진행했을 경우, 지나갈 수 있는 길임을 1로 리턴
            return 1
        if arr[now + 1] == floor:
            # 현재 칸과 다음 칸의 높이가 같을 경우 1칸 진행
            now += 1
        elif now + 1 + L <= len(arr) and arr[now + L] == floor - 1:
            # 다음 칸이 더 낮을 경우 경사로를 놓기 적당한지 판단
            for i in range(L):
                if arr[now + 1 + i] != floor - 1:
                    # 현재 위치에서 경사로 길이만큼 탐색하여 경사로를 놓기 적당하지 않으면 flag = 0
                    flag = 0
                sloped[now + 1 + i] = 1  # 경사로 위치 표시
            now += L
            floor = arr[now]
        elif 0 <= now + 1 - L and arr[now + 1] == floor + 1:
            # 다음 칸의 높이가 더 높을 경우 뒤쪽으로 경사로 길이만큼 탐색하여 경사로를 놓기 적당한지 판단
            for i in range(L):
                # 평평하지 않거나, 이미 경사로가 놓아져 있을 경우 flag = 0
                if sloped[now - i] == 1:
                    flag = 0
                if arr[now - i] != floor:
                    flag = 0
                sloped[now - i] = 1
            now += 1
            floor = arr[now]
        else:
            flag = 0
    return 0


print(solve(matrix))
