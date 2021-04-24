import sys

n, c = map(int, sys.stdin.readline().split())
weight = list(map(int, sys.stdin.readline().split()))
aw = weight[:n // 2]
bw = weight[n // 2:]
asum = []
bsum = []


def bruteforce(warr, sumarr, l, w):
    if l >= len(warr):
        sumarr.append(w)
        return
    bruteforce(warr, sumarr, l + 1, w)
    bruteforce(warr, sumarr, l + 1, w + warr[l])


def binarysearch(arr, target, start, end):
    while start < end:
        mid = (start + end) // 2
        if arr[mid] <= target:
            start = mid + 1
        else:
            end = mid
    return end


bruteforce(aw, asum, 0, 0)
bruteforce(bw, bsum, 0, 0)
bsum.sort()

cnt = 0
for i in asum:
    if c - i < 0:
        continue
    cnt += binarysearch(bsum, c - i, 0, len(bsum))
print(cnt)