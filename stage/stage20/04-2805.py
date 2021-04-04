import sys

n, need = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
minh = 0
maxh = max(trees)


def cut(h):
    length = 0
    for i in trees:
        if i > h:
            length += i - h
    return length


def binarysearch(minh, maxh, target):
    midh = (minh + maxh) // 2
    if minh >= maxh - 1:
        return minh
    if cut(midh) < target:
        return binarysearch(minh, midh, target)
    else:
        return binarysearch(midh, maxh, target)


print(binarysearch(minh, maxh, need))