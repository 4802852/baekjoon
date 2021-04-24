import sys

n, s = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

length = float('inf')
left, right = 0, 0
tmp = nums[left]
while 1:
    if tmp < s:
        right += 1
        if right == n:
            break
        tmp += nums[right]
    else:
        length = min(length, right - left + 1)
        tmp -= nums[left]
        left += 1
print(0 if length == float('inf') else length)