import sys

n = int(sys.stdin.readline())
r = sys.stdin.readline().split()
max = 0
total = 0
for i in range(n):
    if int(r[i]) > max:
        max = int(r[i])
for i in range(len(r)):
    total += int(r[i]) / max * 100
mean = total/len(r)
print(mean)
