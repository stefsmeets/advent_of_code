import numpy as np
import networkx as nx

filename = 'data.txt'

with open(filename) as f:
    lines = f.readlines()

cavern = np.array([[int(val) for val in line.strip()] for line in lines])

def solve(grid):
    imax, jmax = np.array(grid.shape)

    G = nx.grid_2d_graph(imax, jmax, create_using=nx.DiGraph)

    for i, j in G.edges():
        G[i][j]['weight'] = grid[j]

    return nx.shortest_path_length(G, (0, 0), (imax-1, jmax-1), weight='weight')

print(f'part 1: {solve(cavern)=}')

i, j = np.array(cavern.shape)

big_cavern = np.tile(cavern, (5,5))
add = np.sum(np.mgrid[:5,:5], axis=0)
big_cavern += add.repeat(i, axis=0).repeat(j, axis=1)

big_cavern = np.where(big_cavern > 9, big_cavern-9, big_cavern)

print(f'part 2: {solve(big_cavern)=}')
