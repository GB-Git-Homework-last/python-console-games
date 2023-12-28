def print_chess_board(chess_board):
    letters = 'ABCDEFGH'
    print(' +', '-' * 24, '+', sep='')
    for i in range(len(chess_board)):
        print(f'{len(chess_board) - i}|', end='')
        for j in range(len(chess_board)):
            print(f' {chess_board[i][j]} ', end='')
        print('|')
    print(' +', '-' * 24, '+\n   ', sep='', end='')
    for letter in letters:
        print(f'{letter}  ', end='')


def change_chess_board(board, row, col):
    for i in range(SIZE):
        for j in range(SIZE):
            if (i == row or j == col) or (i == j - col + row or j == col + row - i):
                board[i][j] = '.'


def copy_board(old_board):
    new_board = [[' ' for _ in range(SIZE)] for _ in range(SIZE)]
    for i in range(SIZE):
        new_board[i] = old_board[i].copy()
    return new_board


def put_queen(board: list, row: int):
    global SIZE
    global count
    if row == SIZE:
        count += 1
        print(f'\n\nVariant {count}:')
        print_chess_board(board)
        return
    for col in range(SIZE):
        if board[row][col] == ' ':
            new_board = copy_board(board)
            change_chess_board(new_board, row, col)
            new_board[row][col] = 'Ф'
            put_queen(new_board, row + 1)


count = 0
SIZE = 8
chess_board = [[' ' for _ in range(SIZE)] for _ in range(SIZE)]
put_queen(chess_board, 0)
