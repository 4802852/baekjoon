import sys

n = int(sys.stdin.readline())
distance = list(map(int, sys.stdin.readline().split()))
fuel = list(map(int, sys.stdin.readline().split()))
minfuel = 1000000001
ans = 0
for i in range(0, n - 1):
    if fuel[i] <= minfuel:
        minfuel = fuel[i]
    ans += minfuel * distance[i]
print(ans)