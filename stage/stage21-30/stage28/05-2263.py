import sys

sys.setrecursionlimit(10 ** 9)
n = int(sys.stdin.readline())
inorder = list(map(int, sys.stdin.readline().split()))
postorder = list(map(int, sys.stdin.readline().split()))
preorder = []
index = [0] * (n + 1)
for i in range(n):
    index[inorder[i]] = i


def preorderset(iStart, iEnd, pStart, pEnd):
    if (iStart > iEnd) or (pStart > pEnd):
        return
    parent = postorder[pEnd]
    preorder.append(parent)
    parentIndex = index[parent]

    left = parentIndex - iStart
    right = iEnd - parentIndex

    preorderset(iStart, iStart + left - 1, pStart, pStart + left - 1)
    preorderset(iEnd - right + 1, iEnd, pEnd - right, pEnd - 1)


preorderset(0, n - 1, 0, n - 1)
print(*preorder)