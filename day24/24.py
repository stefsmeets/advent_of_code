filename = 'data.txt'

with open(filename) as f:
    lines = list(f.readlines())

def parse(rows):
    return [int(row.split()[-1]) for row in rows]


VALUES = list(
    zip(
        parse(lines[4::18]), 
        parse(lines[5::18]), 
        parse(lines[15::18]),
    ))


def algorithm(w, z=0, *, a, b, c):
    x = int((z % 26) + b != w)
    z //= a
    z *= 25*x+1
    z += (w+c)*x
    return z


def validate(numbers):
    numbers = [int(val) for val in numbers]
    z = 0
    for number, (A, B, C) in zip(numbers, VALUES):
        z = algorithm(number, z, a=A, b=B, c=C)
    return z


order = []
rules = dict()

for idx_right, (a,b,c) in enumerate(VALUES):
    if a == 1:
        # push
        order.append((idx_right, b, c))
    else:
        # pop
        idx_left, b_left, c_left = order.pop()

        diff = c_left + b

        rules[idx_left] = (idx_left, -diff)
        rules[idx_right] = (idx_right, diff)


def find_model_number(smallest=False):
    # smallest=False -> find largest model number
    numbers = {}

    for idx_left in range(14):
        if idx_left in numbers:
            continue

        idx_right, diff = rules[idx_left]

        r = range(1,10)
        if not smallest:
            r = reversed(r)

        for val_left in r:
            val_right = val_left + diff
            if (1 <= val_right <= 9):
                numbers[idx_left] = val_left
                numbers[idx_right] = val_right
                break


    answer = ''.join([str(numbers[i]) for i in range(14)])
    assert validate(answer) == 0
    return answer


print(f'part 1: {find_model_number(smallest=False)=}')
print(f'part 2: {find_model_number(smallest=True)=}')
