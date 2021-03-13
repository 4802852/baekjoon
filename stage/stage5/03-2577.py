import sys

n = []
for i in range(10):
    n.append(0)
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
times = str(a * b * c)
for i in range(len(times)):
    n[int(times[i])] += 1
for i in range(10):
    print(n[i])