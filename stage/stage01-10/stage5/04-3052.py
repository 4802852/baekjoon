import sys

n = []
a = []
count = 0
for i in range(42):
    n.append(0)
for i in range(10):
    a.append(int(sys.stdin.readline()))
for i in range(len(a)):
    n[int(a[i]) % 42] += 1
for i in range(len(n)):
    if n[i] != 0:
        count += 1

print(count)