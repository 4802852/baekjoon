import sys


n = int(sys.stdin.readline())
count = 1
start = 666
while count != n:
    start += 1
    start_list = list(str(start))
    cnt = False
    for i in range(len(start_list) - 2):
        if start_list[i] == start_list[i + 1] == start_list[i + 2] == '6':
            cnt = True
    if cnt is True:
        count += 1

print(start)