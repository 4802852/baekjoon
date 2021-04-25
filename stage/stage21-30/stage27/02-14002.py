import sys

n = int(sys.stdin.readline())
a = [0] + list(map(int, sys.stdin.readline().split()))
dp = [[0, []] for _ in range(n + 1)]
for i in range(1, n + 1):
    tmp = [0, []]
    for j in range(i):
        if a[j] < a[i]:
            if dp[j][0] > tmp[0]:
                tmp[0] = dp[j][0]
                tmp[1] = dp[j][1]
    dp[i][0] = tmp[0] + 1
    dp[i][1] = tmp[1] + [a[i]]
dp.sort()
print(dp[-1][0])
print(*dp[-1][1])