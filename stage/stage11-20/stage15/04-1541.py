import sys

n = sys.stdin.readline().rstrip()
a = list(n.split('-'))
b = []
for i in range(len(a)):
    temp = list(map(int, a[i].split('+')))
    b.append(sum(temp))
ans = b[0]
for j in range(1, len(b)):
    ans -= b[j]
print(ans)