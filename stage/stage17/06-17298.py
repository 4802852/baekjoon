import sys

n = int(sys.stdin.readline())
m = list(map(int, sys.stdin.readline().split()))
stack = []
ans = [-1 for _ in range(n)]
for i in range(n):
    while stack and m[stack[-1]] < m[i]:
        ans[stack.pop()] = m[i]
    stack.append(i)
print(*ans)


# n = int(sys.stdin.readline())
# m = list(map(int, sys.stdin.readline().split()))
# NGE = []
# for i in range(n):
#     for j in range(i + 1, n + 1):
#         if j == n:
#             NGE.append(-1)
#         else:
#             if m[i] < m[j]:
#                 NGE.append(m[j])
#                 break
# for j in NGE:
#     print(j, end=' ')
