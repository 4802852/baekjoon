import sys


n = int(sys.stdin.readline())
array = []
for i in range(n):
    a = int(sys.stdin.readline())
    array.append(a)
array.sort()
for i in range(len(array)):
    print(array[i])