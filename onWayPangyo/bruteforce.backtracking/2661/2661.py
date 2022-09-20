import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

N = int(input())
arr = []


def backtracking(idx):
    for i in range(1, (idx // 2) + 1):
        if arr[-i:] == arr[-2 * i : -i]:
            return -1
    if idx == N:
        for n in arr:
            print(n, end="")
        print()
        return 0

    for i in range(1, 4):
        arr.append(i)
        if backtracking(idx + 1) == 0:
            return 0
        arr.pop()


backtracking(0)
