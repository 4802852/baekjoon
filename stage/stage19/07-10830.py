import sys


def multiply(matrix1, matrix2):
    ans = []
    for i in range(len(matrix1)):
        ans.append([])
        for j in range(len(matrix2[0])):
            temp = 0
            for k in range(len(matrix1[0])):
                temp += matrix1[i][k] * matrix2[k][j]
            ans[i].append(temp % 1000)
    return ans


def power(matrix, p):
    if p == 1:
        return matrix
    else:
        temp = power(matrix, p // 2)
        if p % 2 == 0:
            return multiply(temp, temp)
        else:
            return multiply(multiply(temp, temp), matrix)


n, b = map(int, sys.stdin.readline().split())
m = []
for _ in range(n):
    m.append(list(map(int, sys.stdin.readline().split())))
# check = []
# powerm = []
# while b != 0:
#     check.append(b % 2)
#     b //= 2
#     if not powerm:
#         powerm.append(m)
#     else:
#         powerm.append(multiply(powerm[-1], powerm[-1]))
# k = check.index(1)
# result = powerm[k][:]
# for i in range(k + 1, len(powerm)):
#     if check[i] == 1:
#         result = multiply(result, powerm[i])
result = power(m, b)
for i in range(len(result)):
    temp = []
    for j in range(len(result[i])):
        temp.append(result[i][j] % 1000)
    print(*temp)
