import sys

n = int(sys.stdin.readline())
time = list(map(int, sys.stdin.readline().split()))
time.sort()
ans = 0
for i in range(n):
    for j in range(i + 1):
        ans += time[j]
print(ans)