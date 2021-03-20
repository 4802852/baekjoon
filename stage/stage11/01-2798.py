import sys


n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
sum = 0
for i in range(len(a) - 2):
    for j in range(i + 1, len(a) - 1):
        for k in range(j + 1, len(a)):
            sum_new = a[i] + a[j] + a[k]
            if sum < sum_new <= m:
                sum = sum_new
print(sum)