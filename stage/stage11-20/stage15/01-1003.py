import sys


fibonacci = []
fibonacci.append([1, 0])
fibonacci.append([0, 1])

n = int(sys.stdin.readline())
for i in range(n):
    m = int(sys.stdin.readline())
    for j in range(m + 1):
        if j < len(fibonacci):
            continue
        x = fibonacci[j - 1][0] + fibonacci[j - 2][0]
        y = fibonacci[j - 1][1] + fibonacci[j - 2][1]
        fibonacci.append([x, y])
    print('{} {}'.format(fibonacci[m][0], fibonacci[m][1]))


# def fibonacci(n):
#     global fibonacci_count
#
#     if n == 0:
#         fibonacci_count[0] += 1
#         return 0
#     elif n == 1:
#         fibonacci_count[1] += 1
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# n = int(sys.stdin.readline())
# for i in range(n):
#     fibonacci_count = [0, 0]
#     m = int(sys.stdin.readline())
#     fibonacci(m)
#     print('{} {}'.format(fibonacci_count[0], fibonacci_count[1]))
