import numpy as np
from scipy import ndimage

filename = 'data.txt'

with open(filename) as f:
    lines = (line.strip() for line in f.readlines())

enhance = np.array([(char== '#') for char in next(lines)], dtype=np.int8)

next(lines)

im = np.array([[(char == '#') for char in line] for line in lines], dtype=np.int8)
im = np.pad(im, 51)


def f(x):
    # https://stackoverflow.com/a/15506055
    idx = x.astype(np.int8).dot(1 << np.arange(x.shape[-1] - 1, -1, -1))
    return enhance[idx]


def step(im, steps):
    for step in range(steps):
        im = ndimage.generic_filter(im, f, size=(3,3))
    return im


print(f'part 1: {step(im, 2).sum()=}')
print(f'part 2: {step(im, 50).sum()=}')
