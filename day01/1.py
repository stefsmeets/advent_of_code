import numpy as np

testdata = np.loadtxt('testdata.txt')
data = np.loadtxt('data.txt')


def num_increasing(arr):
    return np.sum(np.roll(arr, shift=1) < arr)


def num_increasing_window(arr, window=3):
    summed = np.convolve(arr, np.ones(window, dtype=int), 'valid')
    return num_increasing(summed)


# part 1

result = num_increasing(testdata)
assert result == 7

result = num_increasing(data)

print(result)

# part 2

result = num_increasing_window(testdata)
assert result == 5

result = num_increasing_window(data)

print(result)

