import sys

c = 1000000007


def multiply(matrix1, matrix2):
    ans = []
    for i in range(len(matrix1)):
        ans.append([])
        for j in range(len(matrix2[0])):
            temp = 0
            for k in range(len(matrix1[0])):
                temp += matrix1[i][k] * matrix2[k][j]
            ans[i].append(temp % c)
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


n = int(sys.stdin.readline())
m = [[1, 1], [1, 0]]
print(power(m, n)[0][1])