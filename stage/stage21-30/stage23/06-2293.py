import sys

n, m = map(int, sys.stdin.readline().split())
coin = [int(sys.stdin.readline()) for _ in range(n)]
dp = [0 for _ in range(m + 1)]
dp[0] = 1
for i in coin:
    for j in range(i, m + 1):
        if j - i >= 0:
            dp[j] += dp[j - i]
print(dp[m])