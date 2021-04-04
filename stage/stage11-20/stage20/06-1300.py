import sys

n = int(sys.stdin.readline())
target = int(sys.stdin.readline())
cnt = 0


def binarysearch(start, end, target):
    global cnt
    if start > end:
        return start
    mid = (start + end) // 2
    cnt = 0
    for i in range(1, n + 1):
        cnt += min(n, mid // i)
    if cnt < target:
        return binarysearch(mid + 1, end, target)
    else:
        return binarysearch(start, mid - 1, target)


print(binarysearch(1, target, target))
