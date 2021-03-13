import sys

n = []
th = 0
max = 0
for i in range(9):
    n.append(int(sys.stdin.readline()))
for i in range(len(n)):
    if n[i] > max:
        max = n[i]
        th = i + 1
print(max)
print(th)