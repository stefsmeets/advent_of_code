from collections import defaultdict

filename = 'data.txt'

with open(filename) as f:
    lines = f.readlines()

numbers = defaultdict(int)

for line in lines:
    patterns, digits = line.split('|')
    digits = digits.split()

    for digit in digits:
        if len(digit) == 2:
            numbers[1] += 1
        elif len(digit) == 3:
            numbers[7] += 1
        elif len(digit) == 4:
            numbers[4] += 1
        elif len(digit) == 7:
            numbers[8] += 1

print(numbers)
print("answer:", sum(numbers.values()))