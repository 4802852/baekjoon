import sys


def binarysearch(array, start, end, target):
    if start > end:
        return 0
    mid = (start + end) // 2
    if target == array[mid]:
        a = mid
        b = mid
        cnt = 1
        while b < len(array):
            if array[b] != target:
                break
            else:
                cnt += 1
            b += 1
        while a >= 0:
            if array[a] != target:
                break
            else:
                cnt += 1
            a -= 1
        return cnt - 2
    elif target < array[mid]:
        return binarysearch(array, start, mid - 1, target)
    else:
        return binarysearch(array, mid + 1, end, target)


n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))
a.sort()
# ans = []
# for i in b:
#     ans.append(binarysearch(a, 0, len(a) - 1, i))
# print(*ans)
# for i in b:
#     print(binarysearch(a, 0, len(a) - 1, i))
dic = {}
for n in a:
    if n not in dic:
        dic[n] = binarysearch(a, 0, len(a) - 1, n)

print(' '.join(str(dic[c]) if c in dic else '0' for c in b))