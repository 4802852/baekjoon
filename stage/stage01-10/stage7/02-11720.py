import sys

n = int(sys.stdin.readline())
m = sys.stdin.readline()
sum = 0
for i in range(n):
    sum += int(m[i])
print(sum)