n = int(input())
count = 1
last_num = 1
while last_num < n:
    last_num += count * 6
    count += 1
print(count)