import sys

n = int(sys.stdin.readline())
A = [0 for _ in range(502)]
cross = A[:]
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    A[a] = b
dp = A[:]
for i in range(1, len(A)):
    maximum = -1
    for j in range(i):
        if A[j] < A[i]:
            if dp[j] >= maximum:
                maximum = dp[j]
    dp[i] = maximum + 1
print(n - max(dp))