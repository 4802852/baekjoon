import sys

matrix = [[], []]
for i in range(2):
    m, n = map(int, sys.stdin.readline().split())
    for _ in range(m):
        matrix[i].append(list(map(int, sys.stdin.readline().split())))


def multiply(matrix1, matrix2):
    ans = []
    for i in range(len(matrix1)):
        ans.append([])
        for j in range(len(matrix2[0])):
            temp = 0
            for k in range(len(matrix1[0])):
                temp += matrix1[i][k] * matrix2[k][j]
            ans[i].append(temp)
    return ans


ans = multiply(matrix[0], matrix[1])
for j in range(len(ans)):
    print(*ans[j])
