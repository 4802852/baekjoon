import sys


def reverse(a):
    reverse_a = ''
    for i in range(len(a) - 1, -1, -1):
        reverse_a += a[i]
    return reverse_a


a, b = sys.stdin.readline().split()
if int(reverse(a)) > int(reverse(b)):
    print(reverse(a))
else:
    print(reverse(b))