
filename = 'data.txt'

position = 0
depth = 0

with open(filename) as f:
    lines = f.readlines()

lines = (line.split() for line in lines)

for direction, steps in lines:
    steps = int(steps)
    if direction == 'forward':
        position += steps
    elif direction == 'up':
        depth -= steps
    elif direction == 'down':
        depth += steps
    else:
        raise ValueError(direction)

print(f'{position=}, {depth=}')
print(f'{position * depth=}')