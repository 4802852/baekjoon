import sys

n = int(sys.stdin.readline())
points = list(map(int, sys.stdin.readline().split()))

points2 = list(sorted(set(points)))
dic = {points2[i]: i for i in range(len(points2))}
print(*[dic[i] for i in points])
