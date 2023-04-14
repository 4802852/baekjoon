import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

N = int(input())
sang = sorted(list(map(int, input().split())))
M = int(input())
check = list(map(int, input().split()))
res = [0] * M


def binarySearch(s, e, t):
    if s == e:
        return False
    mid = (s + e) // 2
    if sang[mid] == t:
        return True
    elif t < sang[mid]:
        return binarySearch(s, mid, t)
    else:
        return binarySearch(mid + 1, e, t)


for i in range(M):
    if binarySearch(0, N, check[i]):
        res[i] = 1
    else:
        res[i] = 0

print(*res)
