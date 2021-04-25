import sys
from bisect import bisect_left

n = int(sys.stdin.readline())
a = [0] + list(map(int, sys.stdin.readline().split()))
dp = [0 for _ in range(n + 1)]
tmp = [-1000000001]
maxVal = 0

for i in range(1, n + 1):
    if tmp[-1] < a[i]:
        tmp.append(a[i])
        dp[i] = len(tmp) - 1
        maxVal = dp[i]
    else:
        dp[i] = bisect_left(tmp, a[i])
        tmp[dp[i]] = a[i]

print(maxVal)

tmp2 = []
for i in range(n, 0, -1):
    if dp[i] == maxVal:
        tmp2.append(a[i])
        maxVal -= 1
print(*tmp2[::-1])