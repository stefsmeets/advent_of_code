import numpy as np
from scipy.ndimage import generic_filter

filename = 'data.txt'

with open(filename) as f:
    lines = f.readlines()

mapping = {'>': 1, 'v': -1, '.': 0}

field = np.array([[mapping[val] for val in line.strip()] for line in lines])

footprint_east = (1, 3)
footprint_south = (3, 1)


def f_east(array):
    a, b, c = array
    if (b == 1) and (c == 0):
        return 0
    elif (b == 0) and (a == 1):
        return 1
    else:
        return b


def f_south(array):
    return -1*f_east(array.T*-1)


for step in range(1, 1000):
    new_field = field.copy()

    new_field = generic_filter(new_field, f_east, size=footprint_east, mode='wrap')
    new_field = generic_filter(new_field, f_south, size=footprint_south, mode='wrap')

    if np.all(field == new_field):
        break

    field = new_field

print(f'part 1: {step=}')
