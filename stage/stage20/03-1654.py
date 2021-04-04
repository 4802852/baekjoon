import sys

sys.setrecursionlimit(10**6)
n, need = map(int, sys.stdin.readline().split())
lines = []
for _ in range(n):
    lines.append(int(sys.stdin.readline()))
lines.sort()

minl = lines[-1] // need
maxl = sum(lines) // need + 1


def divide(lines, l):
    cnt = 0
    for i in range(len(lines)):
        cnt += lines[i] // l
    return cnt


def binarysearch(minl, maxl, target):
    midl = (minl + maxl) // 2
    if minl >= maxl - 1:
        return minl
    if divide(lines, midl) < target:
        return binarysearch(minl, midl, target)
    else:
        return binarysearch(midl, maxl, target)


print(binarysearch(minl, maxl, need))