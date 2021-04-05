import sys
import heapq

n = int(sys.stdin.readline())
leftheap = []
rightheap = []
for _ in range(n):
    m = int(sys.stdin.readline())
    if len(leftheap) == len(rightheap):
        heapq.heappush(leftheap, (-m, m))
    else:
        heapq.heappush(rightheap, (m, m))

    if rightheap and leftheap[0][1] > rightheap[0][1]:
        left = heapq.heappop(leftheap)[1]
        right = heapq.heappop(rightheap)[1]
        heapq.heappush(rightheap, (left, left))
        heapq.heappush(leftheap, (-right, right))
    print(leftheap[0][1])