from collections import defaultdict

filename = 'data.txt'

with open(filename) as f:
    lines = f.readlines()

pool = [int(val) for val in lines[0].split(',')]

baby_fish = 8

pool_dict = defaultdict(int)

for fish in pool:
    pool_dict[fish] += 1

fish_tracker = {}

for day in range(256):
    new_pool_dict = defaultdict(int)

    for fish, number in pool_dict.items():

        if fish == 0:
            fish = 6
            new_pool_dict[baby_fish] += number
        else:
            fish -= 1

        new_pool_dict[fish] += number

    pool_dict = new_pool_dict

    fish_tracker[day] = sum(number for number in pool_dict.values())

print(f'Part 1: {fish_tracker[79]=}')
print(f'Part 2: {fish_tracker[255]=}')
