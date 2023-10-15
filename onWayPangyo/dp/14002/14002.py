import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

import sys

input = sys.stdin.readline

N = int(input())
arr = [0] + list(map(int, input().split()))
dp = [0] * (N + 1)
priorIndex = [0] * (N + 1)

for i in range(1, N + 1):
    for j in range(i):
        if arr[j] < arr[i]:
            if dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                priorIndex[i] = j

maxVal = max(dp)
maxIndex = dp.index(maxVal)
maxArr = []
while arr[maxIndex] != 0:
    maxArr.append(arr[maxIndex])
    maxIndex = priorIndex[maxIndex]
print(maxVal)
ansArr = ""
while maxArr:
    ansArr += str(maxArr.pop())
    if maxArr:
        ansArr += " "
print(ansArr)
