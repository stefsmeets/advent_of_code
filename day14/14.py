from collections import Counter
from collections import defaultdict
from itertools import pairwise

filename = 'data.txt'

with open(filename) as f:
    lines = (line.strip() for line in f.readlines())

template = next(lines)
next(lines)
rules = (line.split(' -> ') for line in lines)
rules = {tuple(rules[0]): rules[1] for rules in rules}


def solve(template, steps):
    counter = Counter(template)
    pairs = Counter(pairwise(template))

    for step in range(steps):
        new_pairs = defaultdict(int)
        for (left, right), count in pairs.items():
            insert = rules[left, right]
            
            counter[insert] += count

            new_pairs[left, insert] += count
            new_pairs[insert, right] += count

        pairs = new_pairs

    difference = counter.most_common()[0][1] - counter.most_common()[-1][1]
    return difference


print(f'part 1: {solve(template, 10)=}')
print(f'part 2: {solve(template, 40)=}')
