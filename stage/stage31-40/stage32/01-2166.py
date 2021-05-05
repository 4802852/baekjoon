import sys

n = int(sys.stdin.readline())
point = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    point.append([a, b])
xold, yold = point.pop(0)
point.append([xold, yold])
area = 0
while point:
    nx, ny = point.pop(0)
    area += (yold + ny) * (nx - xold) / 2
    xold, yold = nx, ny
print("%.1f" % abs(area))
