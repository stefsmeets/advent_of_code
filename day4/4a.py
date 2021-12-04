import numpy as np

filename = 'data.txt'

with open(filename) as f:
    lines = f.readlines()

moves = [int(val) for val in lines[0].split(',')]

board_data = np.loadtxt(lines[2:], dtype=int)

boards = np.split(board_data, len(board_data) / 5)
marked_boards = [np.ones((5,5), dtype=bool) for board in boards]


def check(marked_board):
    bingo_hor = np.any(np.sum(marked_board, axis=0) == 0)
    bingo_ver = np.any(np.sum(marked_board, axis=1) == 0)

    return bingo_hor or bingo_ver

bingo = False

for move in moves:
    for n, (board, marked_board) in enumerate(zip(boards, marked_boards)):
        marked_board[board == move] = False
        bingo = check(marked_board)

        if bingo:
            break

    if bingo:
        print(f'Bingo! #{n}')
        break

print()
print(board)
print(marked_board)
print()

total = board[marked_board].sum()

print(f'{total=}')
print(f'{move=}')
print(f'{total * move}')
