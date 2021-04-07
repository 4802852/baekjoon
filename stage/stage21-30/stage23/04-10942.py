import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
palindrome = [[0 for _ in range(n)] for __ in range(n)]

for i in range(n):
    palindrome[i][i] = 1
for i in range(n - 1):
    if numbers[i] == numbers[i + 1]:
        palindrome[i][i + 1] = 1
for x in range(2, n):
    for i in range(n - x):
        j = i + x
        if palindrome[i + 1][j - 1] == 1 and numbers[i] == numbers[j]:
            palindrome[i][j] = 1

for _ in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    print(palindrome[a - 1][b - 1])