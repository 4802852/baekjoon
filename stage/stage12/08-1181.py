import sys


n = int(sys.stdin.readline())
array = []
for i in range(n):
    a = list(sys.stdin.readline().rstrip())
    b = [len(a)] + a
    c = tuple(b)
    array.append(c)
array_set = set(array)
array = list(array_set)
array.sort()
for i in range(len(array)):
    print(''.join(array[i][1:]))
