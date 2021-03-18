import sys


k = list(range(2, 10001))
m = k[:]
a = 0
b = m[a]
while m[a] != k[-1]:
    a += 1
    for i in range(a, len(k)):
        if k[i] % b == 0:
            m.remove(k[i])
    b = m[a]
    k = m[:]


m = int(sys.stdin.readline())
n = int(sys.stdin.readline())
min = 10001
sum = 0
for i in range(len(k)):
    if m <= k[i] <= n:
        sum += k[i]
        if k[i] < min:
            min = k[i]
if sum == 0:
    print(-1)
else:
    print(sum)
    print(min)