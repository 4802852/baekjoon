import sys


def binarysearch(array, start, end, target):
    if start > end:
        return 0
    mid = (start + end) // 2
    if target == array[mid]:
        return 1
    elif target < array[mid]:
        return binarysearch(array, start, mid - 1, target)
    else:
        return binarysearch(array, mid + 1, end, target)


n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))
a.sort()
for i in b:
    print(binarysearch(a, 0, len(a) - 1, i))
