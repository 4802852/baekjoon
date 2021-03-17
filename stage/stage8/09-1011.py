import sys


max = [0]
i = 1
while max[-1] < (2**31):
    max.append(max[-1] + i)
    max.append(max[-1] + i)
    i += 1

n = int(sys.stdin.readline())
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    for i in range(1, len(max)):
        if max[i - 1] < (b - a) <= max[i]:
            print(i)
            break