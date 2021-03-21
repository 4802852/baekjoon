import sys


n = int(sys.stdin.readline())
coord = []
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    coord.append([y, x])
coord.sort()
for i in range(len(coord)):
    print('{} {}'.format(coord[i][1], coord[i][0]))