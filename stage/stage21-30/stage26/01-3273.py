import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())

nums.sort()
left, right = 0, n - 1
cnt = 0
while left < right:
    tmp = nums[left] + nums[right]
    if tmp > x:
        right -= 1
    elif tmp < x:
        left += 1
    else:
        cnt += 1
        left += 1
        right -= 1
print(cnt)