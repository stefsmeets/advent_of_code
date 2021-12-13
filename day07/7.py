import numpy as np

filename = 'data.txt'

with open(filename) as f:
    lines = f.readlines()

positions = np.array([int(val) for val in lines[0].split(',')])


def get_min_fuel(positions, factorial=False):
    x0 = positions.min()
    x1 = positions.max()

    moves = np.arange(x0, x1)

    best_fuel = np.inf

    for move in moves:
        offset = np.abs(positions - move)

        if factorial:
            fuel = (offset * (offset+1)) / 2
            fuel = int(fuel.sum())
        else:
            fuel = offset.sum()
            
        if fuel < best_fuel:
            best_fuel = fuel

    return best_fuel

print(f'Part 2: {get_min_fuel(positions)=}')
print(f'Part 1: {get_min_fuel(positions, factorial=True)=}')
