import sys

n = int(sys.stdin.readline())
num = []
for i in range(n):
    num.append(int(sys.stdin.readline()))
gcds = [abs(num[1] - num[0])]


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


for j in range(2, len(num)):
    gcds.append(gcd(abs(num[j] - num[j - 1]), gcds[0]))
gcds.sort()
ans = []
for k in range(1, int(gcds[0] ** 0.5) + 1):
    if gcds[0] % k == 0:
        ans.append(k)
        ans.append(gcds[0] // k)
ans = list(set(ans))
ans.sort()
for l in ans[1:]:
    print(l, end=" ")


# ans = []
# for j in range(2, num[0] + 1):
#     prev = num[0] % j
#     for k in range(1, len(num)):
#         if prev != num[k] % j:
#             break
#         if k == len(num) - 1:
#             ans.append(j)
# for l in ans:
#     print(l, end=" ")
