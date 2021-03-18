import sys


k = list(range(2, 1001))
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


n = int(sys.stdin.readline())
list = list(map(int, sys.stdin.readline().split()))
count = 0
for i in range(n):
    if list[i] in k:
        count += 1
print(count)