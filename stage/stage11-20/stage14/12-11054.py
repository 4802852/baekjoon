import sys

n = int(sys.stdin.readline())
m = [0] + list(map(int, sys.stdin.readline().split())) + [0]
dp1 = [0 for _ in range(n + 2)]
dp2 = dp1[:]
dp = dp1[:]
for i in range(1, n + 1):
    maximum1 = 0
    maximum2 = 0
    for j in range(i):
        if m[j] < m[i]:
            if dp1[j] >= maximum1:
                maximum1 = dp1[j]
        if m[n - j + 1] < m[n - i + 1]:
            if dp2[n - j + 1] >= maximum2:
                maximum2 = dp2[n - j + 1]
    dp1[i] = maximum1 + 1
    dp2[n - i + 1] = maximum2 + 1
for i in range(len(dp1)):
    dp[i] = dp1[i] + dp2[i] - 1
print(max(dp))


