import sys


def kmptable(p):
    n = len(p)
    table = [0] * n
    j = 0
    for i in range(1, n):
        while j > 0 and p[i] != p[j]:
            j = table[j - 1]
        if p[i] == p[j]:
            j += 1
            table[i] = j
    return table


def kmp(s, p):
    j = 0
    cnt = 0
    pos = []
    for i in range(len(s)):
        while j > 0 and s[i] != p[j]:
            j = table[j - 1]
        if s[i] == p[j]:
            j += 1
            if j == len(p):
                cnt += 1
                pos.append(i - len(p) + 2)
                j = table[j - 1]
    return cnt, pos


s = sys.stdin.readline().rstrip()
p = sys.stdin.readline().rstrip()
table = kmptable(p)

cnt, pos = kmp(s, p)
print(cnt)
print(*pos)



# import sys
#
# T = str(sys.stdin.readline().rstrip())
# P = str(sys.stdin.readline().rstrip())
#
# k = P[1:].find(P[0]) + 1
# if k:
#     for i in range(k):
#         if i + k >= len(P):
#             continue
#         if P[i] == P[k + i]:
#             max_length = i + 1
# cnt = 0
# location = []
# i = 0
# while i <= len(T) - len(P):
#     tmp = 0
#     for j in range(len(P)):
#         if T[i + j] == P[j]:
#             tmp += 1
#         else:
#             break
#     if k:
#         if tmp >= k:
#             if tmp == len(P):
#                 cnt += 1
#                 location.append(i + 1)
#             i += k
#         else:
#             if tmp:
#                 i += tmp
#             else:
#                 i += 1
#     else:
#         if tmp == len(P):
#             cnt += 1
#             location.append(i + 1)
#         if tmp:
#             i += tmp
#         else:
#             i += 1
#
# print(cnt)
# print(*location)