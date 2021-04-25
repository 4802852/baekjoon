import sys


n = int(sys.stdin.readline())
p = []
p.append(0)
p.append(0)
for i in range(2, n + 1):
    temp = []
    if i % 2 == 0:
        temp.append(p[i // 2] + 1)
    else:
        temp.append(p[(i - 1) // 2] + 2)
    if i % 3 == 0:
        temp.append(p[i // 3] + 1)
    elif i % 3 == 1:
        temp.append(p[(i - 1) // 3] + 2)
    else:
        temp.append(p[(i - 2) // 3] + 3)
    p.append(min(temp))
print(p[n])