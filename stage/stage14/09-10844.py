import sys


n = int(sys.stdin.readline())
dp = [[0 for _ in range(12)] for __ in range(n)]
dp[0] = [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
for i in range(1, n):
    for j in range(1, 11):
        dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
print(sum(dp[-1]) % 1000000000)