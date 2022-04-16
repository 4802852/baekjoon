import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(BASE_DIR + "/input.txt", "r")

# 아래만 복사

# 주기성이 있다는 것을 짐작하고 작성한 코드
# N = int(input())
# mod = 1000000
# fib = [0, 1]
# i = 2
# while 1:
#     fib.append(fib[i - 2] + fib[i - 1])
#     fib[i] %= mod
#     if fib[i] == fib[1] and fib[i - 1] == fib[0]:
#         break
#     i += 1
# print(fib[N % (i - 1)])

# 피사노 주기를 알고 작성한 코드
N = int(input())
mod = 1000000
fib = [0, 1]
p = mod // 10 * 15
for i in range(2, p):
    fib.append(fib[i - 2] + fib[i - 1])
    fib[i] %= mod
print(fib[N % p])
