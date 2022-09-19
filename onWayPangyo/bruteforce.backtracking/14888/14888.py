import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

N = int(input())
arr = list(map(int, input().split(" ")))
op_num = list(map(int, input().split(" ")))
minVal = float("inf")
maxVal = -float("inf")


def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if a < 0:
        return -(-a // b)
    else:
        return a // b


op_arr = [plus, minus, multiply, divide]


def dfs(idx, value):
    global minVal, maxVal
    if idx == N - 1:
        minVal = min(minVal, value)
        maxVal = max(maxVal, value)
        return

    for i in range(4):
        if op_num[i] > 0:
            op_num[i] -= 1
            dfs(idx + 1, op_arr[i](value, arr[idx + 1]))
            op_num[i] += 1


dfs(0, arr[0])
print(maxVal)
print(minVal)
