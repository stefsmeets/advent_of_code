from collections import defaultdict, Counter

filename = 'data.txt'

with open(filename) as f:
    lines = f.readlines()

def normalize(key):
    return ''.join(sorted(key))

numbers = defaultdict(int)

outputs = []

for line in lines:
    mapping = {}
    reverse_mapping = {}
    
    patterns, digits = line.split('|')
    digits = [normalize(digit) for digit in digits.split()]
    patterns = [normalize(pattern) for pattern in patterns.split()]

    for pattern in patterns:
        # first pass for easy numbers
        if len(pattern) == 2:
            match = 1
        elif len(pattern) == 3:
            match = 7
        elif len(pattern) == 4:
            match = 4
        elif len(pattern) == 7:
            match = 8
        else:
            continue

        mapping[pattern] = match
        reverse_mapping[match] = set(pattern)  

    assert len(reverse_mapping) == 4

    for pattern in patterns:
        # second pass

        s = set(pattern)

        same_1 = s.intersection(reverse_mapping[1])
        same_4 = s.intersection(reverse_mapping[4])

        if len(pattern) == 6:
            
            if len(same_1) == 1:
                match = 6
            elif len(same_4) == 4:
                match = 9
            else:
                match = 0
        elif len(pattern) == 5:
            if len(same_1) == 2:
                match = 3
            elif len(same_4) == 3:
                match = 5
            else:
                match = 2
        else:
            continue

        mapping[pattern] = match
        reverse_mapping[match] = s

    assert len(mapping) == 10

    output = 0

    for i, digit in enumerate(digits):
        digit = normalize(digit)
        number = mapping[digit]

        output += number * (10**(3-i))

    outputs.append(output)

    print(digits, output)

print(sum(outputs))