import numpy as np


filename = 'data.txt'

with open(filename, 'r') as f:
    lines = f.readlines()

bits = np.array([[int(number) for number in line.strip()] for line in lines])

gamma = np.sum(bits==1, axis=0) > np.sum(bits==0, axis=0)
gamma = gamma.astype(int)

epsilon = 1 - gamma

gamma_val = int('0b' + ''.join([str(val) for val in gamma]), 2)
epsilon_val = int('0b' + ''.join([str(val) for val in epsilon]), 2)

power_consumption = gamma_val * epsilon_val

print(f'{gamma_val=}')
print(f'{epsilon_val=}')
print(f'{power_consumption=}')

ncols = bits.shape[1]

oxygen_generator = bits

for ncol in range(ncols):
    col = oxygen_generator[:,ncol]

    zero_count = np.sum(col == 0)
    one_count = np.sum(col == 1)

    most_common = int(one_count >= zero_count)
    oxygen_generator = oxygen_generator[col == most_common]

    if len(oxygen_generator) == 1:
        break   

co2_scrubber = bits

for ncol in range(ncols):
    col = co2_scrubber[:,ncol]

    zero_count = np.sum(col == 0)
    one_count = np.sum(col == 1)

    least_common = int(one_count < zero_count)
    co2_scrubber = co2_scrubber[col == least_common]

    if len(co2_scrubber) == 1:
        break

oxygen_generator_val = int('0b' + ''.join([str(val) for val in oxygen_generator.squeeze()]), 2)
co2_scrubber_val =     int('0b' + ''.join([str(val) for val in co2_scrubber.squeeze()]), 2)

life_support = oxygen_generator_val * co2_scrubber_val

print(f'{oxygen_generator_val=}')
print(f'{co2_scrubber_val=}')
print(f'{life_support=}')
