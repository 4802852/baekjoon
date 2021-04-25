import sys

n = int(sys.stdin.readline())
m = [0] + list(map(int, sys.stdin.readline().split()))
dp = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    maximum = 0
    for j in range(i):
        if m[j] < m[i]:
            if dp[j] >= maximum:
                maximum = dp[j]
    dp[i] = maximum + 1
print(max(dp))