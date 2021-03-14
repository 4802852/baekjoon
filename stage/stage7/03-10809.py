import sys

S = sys.stdin.readline()
ans = [-1] * 26
count = 0
for i in range(len(S) - 1):
    a = ord(S[i]) - 97
    if ans[a] == -1:
        ans[a] = count
    else:
        pass
    count += 1

# ans2 = '{}'.format(ans[0])
# for i in range(1, len(ans)):
#     ans2 += ' {}'.format(ans[i])
#
# print(ans2)

print(*ans)  # unpacking