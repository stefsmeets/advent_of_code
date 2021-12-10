from collections import defaultdict

filename = 'data.txt'

with open(filename) as f:
    lines = f.readlines()

pool = [int(val) for val in lines[0].split(',')]

print(pool)

baby_fish = 8

pool_dict = defaultdict(int)

for fish in pool:
    pool_dict[fish] += 1

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

    print(day, sum(number for number in pool_dict.values()))

print()
print(pool_dict)
print(sum(number for number in pool_dict.values()))
