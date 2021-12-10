import numpy as np
from dataclasses import dataclass

filename = 'data.txt'

@dataclass
class Pipe:
    x1: int
    y1: int
    x2: int
    y2: int

    @property
    def is_horizontal(self):
        return self.x1 == self.x2

    @property
    def is_vertical(self):
        return self.y1 == self.y2

    @property
    def is_diagonal(self):
        return not (self.is_horizontal or self.is_vertical)

    @property
    def xmin(self):
        return min(self.x1, self.x2)

    @property
    def xmax(self):
        return max(self.x1, self.x2)

    @property
    def ymin(self):
        return min(self.y1, self.y2)

    @property
    def ymax(self):
        return max(self.y1, self.y2)



with open(filename) as f:
    lines = f.readlines()

lines = (line.replace('->',',') for line in lines)
lines = (line.split(',') for line in lines)
lines = ([int(val) for val in line] for line in lines)
pipes = [Pipe(*line) for line in lines]

xmax = max([pipe.xmax for pipe in pipes]) + 1
ymax = max([pipe.ymax for pipe in pipes]) + 1

field = np.zeros((xmax, ymax))
print(field.shape)

for pipe in pipes:
    if pipe.is_diagonal:
        continue

    if pipe.is_horizontal:
        field[pipe.xmin, pipe.ymin: pipe.ymax+1] += 1

    if pipe.is_vertical:
        field[pipe.xmin: pipe.xmax+1, pipe.ymin] += 1

print()
print(field)
print(f'{np.sum(field>=2)}')
