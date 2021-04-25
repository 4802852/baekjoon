import sys
from collections import deque

n = int(sys.stdin.readline())
for _ in range(n):
    iserror = False
    a = str(sys.stdin.readline())
    b = int(sys.stdin.readline())
    c = sys.stdin.readline()
    if b > 0:
        d = c[1:-2]
        p = list(map(str, d.split(',')))
        dq = deque(p)
    else:
        dq = deque([])
    left = True
    for i in range(len(a)):
        if a[i] == 'R':
            if left:
                left = False
            else:
                left = True
        if a[i] == 'D':
            if dq:
                if left:
                    dq.popleft()
                else:
                    dq.pop()
            else:
                iserror = True
    if iserror:
        print('error')
    else:
        if left:
            temp = list(dq)
        else:
            temp = list(dq)[::-1]
        print('[' + ','.join(temp) + ']')


# def r(dq):
#     temp = deque([])
#     for _ in range(len(dq)):
#         temp.append(dq.pop())
#     return temp
#
#
# n = int(sys.stdin.readline())
# for _ in range(n):
#     iserror = False
#     a = str(sys.stdin.readline())
#     b = int(sys.stdin.readline())
#     c = sys.stdin.readline()
#     if b > 0:
#         d = c[1:-2]
#         p = list(map(int, d.split(',')))
#         dq = deque(p)
#     else:
#         dq = deque([])
#     for i in range(len(a)):
#         if a[i] == 'R':
#             dq = r(dq)
#         if a[i] == 'D':
#             if dq:
#                 dq.popleft()
#             else:
#                 iserror = True
#     if iserror:
#         print('error')
#     else:
#         print(list(dq))