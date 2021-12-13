filename = 'data.txt'

with open(filename) as f:
    lines = f.readlines()

lines = [line.split() for line in lines]


def get_position(data):
    position = 0
    depth = 0

    for direction, steps in data:
        steps = int(steps)
        if direction == 'forward':
            position += steps
        elif direction == 'up':
            depth -= steps
        elif direction == 'down':
            depth += steps
        else:
            raise ValueError(direction)

    return position, depth


def get_position_with_aim(data):
    position = 0
    depth = 0
    aim = 0

    for direction, steps in data:
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

    return position, depth


# part 1
position1, depth1 = get_position(lines)
print(f'part 1: {position1 * depth1=}')

# part 2
position2, depth2 = get_position_with_aim(lines)
print(f'part 2: {position2 * depth2=}')