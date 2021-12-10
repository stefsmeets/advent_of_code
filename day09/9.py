import numpy as np
import scipy.ndimage as ndi

filename = 'data.txt'

with open(filename) as f:
    lines = f.readlines()

heightmap = np.array([[int(val) for val in line.strip()] for line in lines])

footprint = np.array([
    [0, 1, 0], 
    [1, 0, 1], 
    [0, 1, 0]
])

filtered = ndi.minimum_filter(heightmap, footprint=footprint, mode='constant', cval=999)
lava_tubes = heightmap < filtered

risk = np.sum(heightmap[lava_tubes] + 1)

print(f'{risk=}')

basins, n_basins = ndi.label(heightmap < 9)
basin_sizes = [(basins==i+1).sum() for i in range(n_basins)]

three_largest_basins = sorted(basin_sizes, reverse=True)[0:3]

print(f'{np.product(three_largest_basins)=}')
