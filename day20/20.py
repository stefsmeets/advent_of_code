import numpy as np
from scipy import ndimage

filename = 'data.txt'

with open(filename) as f:
    lines = (line.strip() for line in f.readlines())

algorithm = np.array([(char== '#') for char in next(lines)], dtype=np.int8)

next(lines)

im = np.array([[(char == '#') for char in line] for line in lines], dtype=np.int8)

POWERS = (2 ** np.arange(9))[::-1]


def f(x):
    idx = int((x*POWERS).sum())
    return algorithm[idx]


def enhance(im, steps):
    cval = 0

    for step in range(steps):
        im = np.pad(im, 1, constant_values=cval)
        im = ndimage.generic_filter(im, f, size=(3,3))
        cval = algorithm[[0,-1][cval]]

    return im


print(f'part 1: {enhance(im, 2).sum()=}')
print(f'part 2: {enhance(im, 50).sum()=}')
