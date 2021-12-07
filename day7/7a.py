import numpy as np

filename = 'data.txt'

with open(filename) as f:
    lines = f.readlines()

positions = np.array([int(val) for val in lines[0].split(',')])

x0 = positions.min()
x1 = positions.max()

moves = np.arange(x0, x1)

best_fuel = np.inf
best_move = -1

for move in moves:
    fuel = np.sum(np.abs(positions - move))

    if fuel < best_fuel:
        best_move = move
        best_fuel = fuel

print(f'{best_move=}, {best_fuel=}')
