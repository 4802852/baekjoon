import sys

n = int(input())
l = sys.stdin.readline().split()
max = -1000001
min = 1000001
for i in range(n):
    if int(l[i]) > max:
        max = int(l[i])
    if int(l[i]) < min:
        min = int(l[i])
print('{} {}'.format(min, max))