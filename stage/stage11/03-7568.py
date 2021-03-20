import sys


n = int(sys.stdin.readline())
member = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    member.append([a, b])
stat = [1] * n
for i in range(len(member)):
    for j in range(i, len(member)):
        if member[i][0] > member[j][0] and member[i][1] > member[j][1]:
            stat[j] += 1
        elif member[i][0] < member[j][0] and member[i][1] < member[j][1]:
            stat[i] += 1
stat2 = []
for i in range(len(stat)):
    stat2.append(str(stat[i]))
print(' '.join(stat2))