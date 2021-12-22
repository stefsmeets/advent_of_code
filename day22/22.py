from dataclasses import dataclass
from collections import Counter

filename = 'data.txt'

with open(filename) as f:
    lines = f.readlines()

def grab_range(val, line):
    part = line[line.index(f'{val}=')+2:].split(',')[0]
    minval, maxval = [int(val) for val in part.split('..')]
    return minval, maxval


def count(cubes):
    return sum(box.volume * sign for box, sign in cubes.items())


@dataclass
class Box:
    x0: int
    x1: int
    y0: int
    y1: int
    z0: int
    z1: int

    def __hash__(self):
        return hash((self.x0, self.x1, self.y0, self.y1, self.z0, self.z1))

    @classmethod
    def from_line(cls, line):
        switch, ranges = line.split(maxsplit=1)
        xvals = grab_range('x', ranges)
        yvals = grab_range('y', ranges)
        zvals = grab_range('z', ranges)

        return switch=='on', cls(*xvals, *yvals, *zvals)

    @property
    def volume(self):
        if self.x1 < self.x0:
            return -1
        if self.y1 < self.y0:
            return -1
        if self.z1 < self.z0:
            return -1
        return (self.x1 - self.x0 + 1) * (self.y1 - self.y0 + 1) * (self.z1 - self.z0 + 1)

    def intersection(self, other):
        x0 = max(self.x0, other.x0)
        y0 = max(self.y0, other.y0)
        z0 = max(self.z0, other.z0)
        x1 = min(self.x1, other.x1)
        y1 = min(self.y1, other.y1)
        z1 = min(self.z1, other.z1)

        return self.__class__(x0, x1, y0, y1, z0, z1)


boxes = [Box.from_line(line) for line in lines]
subregion = Box(-50, 50, -50, 50, -50, 50)

cubes_all = Counter()
cubes_subregion = Counter()

for switch, box in boxes:
    intersect_boxes = Counter()
    for other, other_sign in cubes_all.items():
        intersection = box.intersection(other)

        if intersection.volume > 0:
            intersect_boxes[intersection] -= other_sign
    
    intersect_boxes[box] += switch
    cubes_all.update(intersect_boxes)

    # part 1
    if box.intersection(subregion).volume > 0:
        cubes_subregion.update(intersect_boxes)


print(f'part 1: {count(cubes_subregion)=}')
print(f'part 2: {count(cubes_all)=}')
