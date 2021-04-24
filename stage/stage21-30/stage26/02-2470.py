import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

nums.sort()
left, right = 0, n - 1
ans = [float('inf'), 0, 0]
while left < right:
    tmp = nums[left] + nums[right]
    if abs(tmp) < ans[0]:
        ans = [abs(tmp), nums[left], nums[right]]
    if tmp > 0:
        right -= 1
    elif tmp < 0:
        left += 1
    else:
        ans = [abs(tmp), nums[left], nums[right]]
        break
print('{} {}'.format(ans[1], ans[2]))
