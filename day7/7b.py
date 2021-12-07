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

def calc_fuel(offset):
    return np.arange(offset + 1).sum()

for move in moves:
    offset = positions - move
    fuel = np.apply_along_axis(calc_fuel, 1, np.abs(offset).reshape(-1,1))
    fuel = fuel.sum()

    if fuel < best_fuel:
        best_move = move
        best_fuel = fuel

print(f'{best_move=}, {best_fuel=}')
