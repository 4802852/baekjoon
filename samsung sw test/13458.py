import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
ans = 0
for i in range(N):
    now = A[i]
    if now:
        now -= B
        ans += 1
        if now > 0:
            ans += now // C
            now %= C
        if now > 0:
            ans += 1
print(ans)
