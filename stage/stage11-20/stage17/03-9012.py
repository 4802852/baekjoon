import sys

n = int(sys.stdin.readline())
for i in range(n):
    m = list(map(str, sys.stdin.readline().rstrip()))
    vps = 0
    for j in range(len(m)):
        if vps < 0:
            break
        if m[j] == '(':
            vps += 1
        else:
            vps -= 1
    if vps == 0:
        print('YES')
    else:
        print('NO')