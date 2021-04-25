import sys


sudoku = []
for i in range(9):
    a = list(map(int, sys.stdin.readline().split()))
    sudoku.append(a)
zeros = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]
ans = False


def check(i, j):
    pool = [i for i in range(1, 10)]
    for k in range(9):
        if sudoku[i][k] in pool:
            pool.remove(sudoku[i][k])
        if sudoku[k][j] in pool:
            pool.remove(sudoku[k][j])
    i //= 3
    j //= 3
    for p in range(i * 3, (i + 1) * 3):
        for q in range(j * 3, (j + 1) * 3):
            if sudoku[p][q] in pool:
                pool.remove(sudoku[p][q])
    return pool


def solve_sudoku(x):
    global ans
    if ans:
        return
    if x == len(zeros):
        for row in sudoku:
            print(*row)
        ans = True
        return
    else:
        (i, j) = zeros[x]
        possible = check(i, j)
        for num in possible:
            sudoku[i][j] = num
            solve_sudoku(x + 1)
            sudoku[i][j] = 0


solve_sudoku(0)