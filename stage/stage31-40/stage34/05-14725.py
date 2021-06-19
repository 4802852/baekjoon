import sys

n = int(sys.stdin.readline())
array = []
for _ in range(n):
    tmp = list(sys.stdin.readline().split())
    array.append(tmp[1:])
array.sort()

for j in range(len(array[0])):
    print("--" * j + array[0][j])
for i in range(1, n):
    count = -1
    for j in range(len(array[i])):
        if len(array[i - 1]) <= j or array[i - 1][j] != array[i][j]:
            break
        else:
            count = j
    for j in range(count + 1, len(array[i])):
        print("--" * j + array[i][j])
