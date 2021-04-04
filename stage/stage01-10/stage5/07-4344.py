import sys

n = int(sys.stdin.readline())
for i in range(n):
    a = sys.stdin.readline().split()
    total = 0
    for i in range(1, len(a)):
        total += int(a[i])
    mean = total / int(a[0])
    count = 0
    for i in range(1, len(a)):
        if int(a[i]) > mean:
            count += 1
    result = count / int(a[0]) * 100
    print('%.3f' % result + '%')