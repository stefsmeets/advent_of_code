
filename = 'data.txt'

position = 0
depth = 0
aim = 0

with open(filename) as f:
    lines = f.readlines()

lines = (line.split() for line in lines)

for direction, steps in lines:
    steps = int(steps)
    if direction == 'forward':
        position += steps
        depth += steps * aim
    elif direction == 'up':
        aim -= steps
    elif direction == 'down':
        aim += steps
    else:
        raise ValueError(direction)

print(f'{position=}, {depth=}')
print(f'{position * depth=}')