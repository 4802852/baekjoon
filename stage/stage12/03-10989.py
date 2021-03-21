import sys


n = int(sys.stdin.readline())
array = [0] * 10001
for i in range(n):
    a = int(sys.stdin.readline())
    array[a] += 1
for i in range(len(array)):
    if array[i] > 0:
        for j in range(array[i]):
            print(i)