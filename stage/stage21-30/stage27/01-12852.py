import sys

n = int(sys.stdin.readline())
dp = [[0, []] for _ in range(n + 1)]
dp[1][1] = [1]
for i in range(2, n + 1):
    dp[i][0] = dp[i - 1][0] + 1
    dp[i][1] = dp[i - 1][1] + [i]
    if i % 3 == 0 and dp[i // 3][0] + 1 < dp[i][0]:
        dp[i][0] = dp[i // 3][0] + 1
        dp[i][1] = dp[i // 3][1] + [i]
    if i % 2 == 0 and dp[i // 2][0] + 1 < dp[i][0]:
        dp[i][0] = dp[i // 2][0] + 1
        dp[i][1] = dp[i // 2][1] + [i]
print(dp[n][0])
tmp = dp[n][1][::-1]
print(*tmp)

n = int(sys.stdin.readline())
dp = []
dp.append([0])
dp.append([0])
for i in range(2, n + 1):
    temp = []
    if i % 2 == 0:
        temp.append([dp[i // 2][0] + 1, i // 2])
    else:
        temp.append([dp[(i - 1) // 2][0] + 2, i - 1, (i - 1) // 2])
    if i % 3 == 0:
        temp.append([dp[i // 3][0] + 1, i // 3])
    elif i % 3 == 1:
        temp.append([dp[(i - 1) // 3][0] + 2, i - 1, (i - 1) // 3])
    else:
        temp.append([dp[(i - 2) // 3][0] + 3, i - 1, i - 2, (i - 2) // 3])
    temp.sort()
    dp.append(temp[0])
print(dp[n][0])
tmp = n
arr = [n]
while tmp != 1:
    for i in range(1, len(dp[tmp])):
        arr.append(dp[tmp][i])
    tmp = dp[tmp][-1]
print(*arr)