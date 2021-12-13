import numpy as np

filename = 'tweakers.input'

with open(filename) as f:
    lines = (line.strip() for line in f.readlines())

dots = []
folds = []

for line in lines:
    if line.startswith('fold along'):
        direction, line_no = line.split()[-1].split('=')
        line_no = int(line_no)
        folds.append((direction, line_no))
    elif line:
        dots.append([int(val) for val in line.split(',')])

dots = np.array(dots)

shape = dots.max(axis=0) + 1
grid = np.zeros(shape)

grid[dots[:,0], dots[:,1]] = 1

for i, (direction, line_no) in enumerate(folds):
    if direction == 'y':
        slice_1 = np.s_[:, :line_no]
        slice_2 = np.s_[:, line_no+1:]
        flip = np.fliplr
    else:
        slice_1 = np.s_[:line_no]
        slice_2 = np.s_[line_no+1:]        
        flip = np.flipud

    folded = flip(grid[slice_2])
    grid = grid[slice_1]

    if direction == 'y':
        start = grid.shape[1] - folded.shape[1]
        grid[:, start:] += folded
    else:
        start = grid.shape[0] - folded.shape[0]
        grid[start:] += folded
        
    if i == 0:
        n_dots_first_fold = np.sum(grid>0)


print(f'part 1: {n_dots_first_fold=}')

import matplotlib.pyplot as plt
plt.imshow((grid>0).T)
plt.title('Part 2')
plt.show()

