import sys

n = int(sys.stdin.readline())
board = []
for _ in range(n):
    board.append(list(sys.stdin.readline().rstrip()))
compression = []


def cut(x, y, n):
    check = board[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != board[i][j]:
                compression.append('(')
                cut(x, y, n // 2)
                cut(x, y + n // 2, n // 2)
                cut(x + n // 2, y, n // 2)
                cut(x + n // 2, y + n // 2, n // 2)
                compression.append(')')
                return
    if check == '0':
        compression.append('0')
        return
    else:
        compression.append('1')
        return


cut(0, 0, n)
print(''.join(compression))