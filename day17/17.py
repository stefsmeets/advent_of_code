from dataclasses import dataclass

filename = 'data.txt'

with open(filename) as f:
    line = f.readline()

def grab_range(val, line):
    part = line[line.index(f'{val}=')+2:].split(',')[0]
    minval, maxval = [int(val) for val in part.split('..')]
    return minval, maxval

x_min, x_max = grab_range('x', line)
y_min, y_max = grab_range('y', line)

DRAG = 1
GRAVITY = 1

ON_THE_WAY = '🚀'
BOMBED = '💣'
BULLSEYE = '🎯'

@dataclass
class Probe:
    vx: int
    vy: int
    x: int = 0
    y: int = 0
    highest_y: int = 0

    def step(self):
        self.x += self.vx
        self.y += self.vy

        if self.y > self.highest_y:
            self.highest_y = self.y

        if self.vx > 0:
            self.vx -= DRAG
        if self.vx < 0:
            self.vx += DRAG

        self.vy -= GRAVITY

    def status(self):
        if (self.x > x_max) or (self.y < y_min):
            return BOMBED
        elif (self.x >= x_min) and (self.x <= x_max) and (self.y <= y_max) and (self.y >= y_min):
            return BULLSEYE
        else:
            return ON_THE_WAY

    def run_until_end(self):
        while self.status() == ON_THE_WAY:
            self.step()

        return self.status() == BULLSEYE


success = []

for vx in range(0, 70):
    for vy in range(-300, 300):
        p = Probe(vx, vy)
        if p.run_until_end():
            success.append(p)

print(f'part 1: {max([p.highest_y for p in success])=}')
print(f'part 2: {len(success)}')
