import numpy as np
from scipy import ndimage

filename = 'data.txt'

with open(filename) as f:
    lines = (line.strip() for line in f.readlines())

mapping = {'.': 0, '#': 1}

enhance = [mapping[char] for char in next(lines)]
next(lines)

im = np.array([[mapping[char] for char in line] for line in lines])


def f(x):
    idx = int('0b' + ''.join([str(val) for val in x.astype(int)]), 2)
    return enhance[idx]


def step(im, steps):
    cval = 0

    for step in range(steps):
        im = np.pad(im, 1, constant_values=cval)
        im = ndimage.generic_filter(im, f, size=(3,3))
        cval = enhance[[0,-1][cval]]

    return im


print(f'part 1: {step(im, 2).sum()=}')
print(f'part 2: {step(im, 50).sum()=}')

breakpoint()