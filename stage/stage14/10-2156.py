import sys

n = int(sys.stdin.readline())
max_wine = [[0, 0, 0] for _ in range(n + 1)]
wine = [0 for __ in range(n + 1)]
for i in range(1, n + 1):
    wine[i] = int(sys.stdin.readline())
max_wine[1] = [wine[1], wine[1], wine[1]]
if n > 1:
    max_wine[2] = [wine[2], wine[2], wine[1] + wine[2]]
if n > 2:
    for j in range(3, n + 1):
        max_wine[j][0] = max(max_wine[j - 3]) + wine[j]
        max_wine[j][1] = max(max_wine[j - 2]) + wine[j]
        max_wine[j][2] = max(max_wine[j - 1][0], max_wine[j - 1][1]) + wine[j]
a = max_wine[-1] + max_wine[-2]
print(max(a))