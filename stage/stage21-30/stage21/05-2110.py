import sys

n, c = map(int, sys.stdin.readline().split())
x = []
for _ in range(n):
    x.append(int(sys.stdin.readline()))
x.sort()


def router(d):
    cnt = 1
    prev = x[0]
    for i in range(1, len(x)):
        if prev + d <= x[i]:
            prev = x[i]
            cnt += 1
    return cnt


def binarysearch(mind, maxd, target):
    midd = (mind + maxd) // 2
    if mind >= maxd - 1:
        return mind
    if router(midd) < target:
        return binarysearch(mind, midd, target)
    else:
        return binarysearch(midd, maxd, target)


print(binarysearch(1, (x[-1] - x[0]) // (c - 1) + 1, c))
