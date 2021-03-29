import sys

m = [0] + list(sys.stdin.readline().rstrip())
n = [0] + list(sys.stdin.readline().rstrip())
dp = [[0 for _ in range(1002)] for __ in range(1002)]
for i in range(1, len(m)):
    for j in range(1, len(n)):
        if m[i] == n[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
print(dp[len(m) - 1][len(n) - 1])