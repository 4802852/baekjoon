import sys

n = int(sys.stdin.readline())
for i in range(n):
    r, a = sys.stdin.readline().split()
    ans = ''
    for j in range(len(a)):
        for k in range(int(r)):
            ans += '{}'.format(a[j])
    print(ans)