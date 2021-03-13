import sys

n = int(sys.stdin.readline())
for i in range(n):
    a = sys.stdin.readline()
    total = 0
    now = 0
    prev = 'X'
    for i in range(len(a)):
        if a[i] == 'O':
            now += 1
            total += now
        else:
            now = 0
    print(total)