import sys

n = int(sys.stdin.readline())
m = [0] + list(map(int, sys.stdin.readline().split()))
dp = [-1001 for _ in range(n + 1)]
for i in range(1, n + 1):
    dp[i] = max(dp[i - 1] + m[i], m[i])
print(max(dp))