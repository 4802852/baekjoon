import sys


n = int(sys.stdin.readline())
array = []
for i in range(n):
    a = int(sys.stdin.readline())
    array.append(a)
array_mean = round(sum(array) / len(array))
array_median = sorted(array)[n // 2]
counter = [0] * 8001
for i in range(len(array)):
    counter[array[i]] += 1
counter_max = max(counter)
array_mode = []
for i in range(len(counter)):
    if counter[i] == counter_max:
        num = i
        if num > 4000:
            num -= 8001
        array_mode.append(num)
array_mode.sort()
if len(array_mode) > 1:
    array_mode2 = array_mode[1]
else:
    array_mode2 = array_mode[0]
array_range = max(array) - min(array)
print(array_mean)
print(array_median)
print(array_mode2)
print(array_range)