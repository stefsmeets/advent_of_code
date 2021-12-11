import numpy as np

filename = 'data.txt'

with open(filename) as f:
    lines = f.readlines()

grid = np.array([[int(val) for val in line.strip()] for line in lines])

def get_adjecent(index):
    i, j = index
    n = 1
    left = max(0, i - n)
    right = max(0, i + n + 1)

    bottom = max(0, j - n)
    top = max(0, j + n + 1)

    return np.s_[left:right, bottom:top]

n_flashes = 0

for step in range(1000):
    grid += 1

    while np.any(flashing_octopi := grid > 9):
        grid[flashing_octopi] = -99

        for octopus in np.argwhere(flashing_octopi):
            n_flashes += 1
            grid[get_adjecent(octopus)] += 1

    grid[grid < 0] = 0

    if step == 99:
        # part 1
        n_flashes_at_100 = n_flashes

    if np.all(grid == 0):
        # part 2
        sync_step = step + 1
        break

print(f'{n_flashes_at_100=}')
print(f'{n_flashes=}')
print(f'{sync_step=}')
