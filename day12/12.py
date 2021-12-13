import networkx as nx

filename = 'data.txt'

with open(filename) as f:
    lines = [line.strip() for line in f.readlines()]

G = nx.Graph()

for line in lines:
    cave, connected = line.split('-')
    G.add_edge(cave, connected)


def get_paths(G, path=['start'], visit_twice=False):
    current_cave = path[-1]
    for cave in G.neighbors(current_cave):
        new_path = path + [cave]
        
        large = cave.isupper()
        not_visited = cave not in path 
        
        starting_cave = cave == 'start'

        if cave == 'end':
            yield new_path
        elif large or not_visited:
            yield from get_paths(G, new_path, visit_twice)
        elif visit_twice and not starting_cave:
            yield from get_paths(G, new_path, visit_twice=False)

# part 1
paths_1 = get_paths(G)
n_paths_1 = sum(1 for path in paths_1)
print(f'{n_paths_1=}')

# part 2
paths_2 = get_paths(G, visit_twice=True)
n_paths_2 = sum(1 for path in paths_2)
print(f'{n_paths_2=}')
