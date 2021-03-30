import sys

n, t = map(int, sys.stdin.readline().split())
coin = []
for _ in range(n):
    coin.append(int(sys.stdin.readline()))
coin.sort(reverse=True)
i = 0
count = 0
while t != 0:
    if t // coin[i] == 0:
        i += 1
    else:
        count += t // coin[i]
        t = t % coin[i]
        i += 1
print(count)