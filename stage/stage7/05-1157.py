# A65Z90  -65
# a97z122 -97

import sys

w = sys.stdin.readline()
list = [0] * 26
for i in range(len(w) - 1):
    if ord(w[i]) > 95:
        list[ord(w[i]) - 97] += 1
    else:
        list[ord(w[i]) - 65] += 1

max = -1
max_check = False
for i in range(len(list)):
    if list[i] > max:
        max = list[i]
        max_cha = i
        max_check = False
    elif list[i] == max:
        max_check = True
    else:
        pass

if max_check is True:
    print('?')
else:
    print(chr(max_cha + 65))