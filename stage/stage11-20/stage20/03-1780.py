import sys

n = int(sys.stdin.readline())
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))
count = [0, 0, 0]  # -1, 0, 1


def cut(x, y, n):
    check = board[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != board[i][j]:
                cut(x, y, n // 3)
                cut(x, y + n // 3, n // 3)
                cut(x, y + 2 * n // 3, n // 3)
                cut(x + n // 3, y, n // 3)
                cut(x + n // 3, y + n // 3, n // 3)
                cut(x + n // 3, y + 2 * n // 3, n // 3)
                cut(x + 2 * n // 3, y, n // 3)
                cut(x + 2 * n // 3, y + n // 3, n // 3)
                cut(x + 2 * n // 3, y + 2 * n // 3, n // 3)
                return
    if check == -1:
        count[0] += 1
        return
    elif check == 0:
        count[1] += 1
        return
    else:
        count[2] += 1
        return


cut(0, 0, n)
print(count[0])
print(count[1])
print(count[2])