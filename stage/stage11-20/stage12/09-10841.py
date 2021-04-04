import sys


n = int(sys.stdin.readline())
array = []
for i in range(n):
    age, name = map(str, sys.stdin.readline().split())
    array.append([int(age), i, name])
array.sort()
for i in range(len(array)):
    print('{} {}'.format(array[i][0], array[i][2]))