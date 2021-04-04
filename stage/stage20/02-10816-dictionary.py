import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

dic = dict()

for i in a:
    try:
        dic[i] += 1
    except:
        dic[i] = 1

for i in b:
    try:
        print(dic[i], end=" ")
    except:
        print(0, end=" ")
