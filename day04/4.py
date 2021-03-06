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

winners = []

for move in moves:
    bingo = False

    for n, (board, marked_board) in enumerate(zip(boards, marked_boards)):
        marked_board[board == move] = False
        bingo = check(marked_board)

        if bingo:
            if len(winners) == 0:
                total = board[marked_board].sum()

                # part 1
                print(f'part 1: {total * move=}')
            
            if n not in winners:
                winners.append(n)

    if len(winners) == len(boards):
        break


winner = winners[-1]
board = boards[winner]
marked_board = marked_boards[winner]
total = board[marked_board].sum()

# part 2
print(f'part 2: {total * move=}')
