import sys

n = int(sys.stdin.readline())
stack = []
op = []
count = 1
isstackarray = True
for i in range(n):
    num = int(sys.stdin.readline())
    while count <= num:
        stack.append(count)
        op.append('+')
        count += 1
    if stack[-1] == num:
        stack.pop()
        op.append('-')
    else:
        isstackarray = False
if isstackarray == False:
    print('NO')
else:
    for j in op:
        print(j)
