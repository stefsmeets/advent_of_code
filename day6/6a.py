filename = 'data.txt'

with open(filename) as f:
    lines = f.readlines()

pool = [int(val) for val in lines[0].split(',')]

print(pool)

baby_fish = 8

for day in range(80):

    new_pool = []

    for fish in pool:
        if fish == 0:
            fish = 6
            new_pool.append(baby_fish)
        else:
            fish -= 1

        new_pool.append(fish)

    pool = new_pool

    print(day, len(pool))

print(len(new_pool))
