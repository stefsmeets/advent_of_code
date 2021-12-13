import numpy as np

data = np.loadtxt('data.txt')

def num_increasing(arr):
    return np.sum(np.roll(arr, shift=1) < arr)

def num_increasing_window(arr, window=3):
    summed = np.convolve(arr, np.ones(window, dtype=int), 'valid')
    return num_increasing(summed)

# part 1
result = num_increasing(data)
print(f'part 1: {num_increasing(data)=}')

# part 2
print(f'part 2: {num_increasing_window(data)=}')
