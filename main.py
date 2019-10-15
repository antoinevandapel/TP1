import numpy as np


arr = np.array([
    [1.2, 2.3, 4.0],
    [1.2, 3.4, 5.2],
    [0.0, 1.0, 1.3],
    [0.0, 1.0, 2e-1]])
print(arr)

print(arr.dtype)
print(arr.ndim)
print(arr.shape)

iarr = np.array([1, 2, 3], np.uint8)

arr *= 2.5
np.multiply(iarr, 2.5)
print(arr)
print(iarr)

is_greater_one = (arr >= 1.)
print(is_greater_one)

print(arr[0,0]) # First row, first column
print(arr[1]) # The whole second row
print(arr[:,2]) # The third column

print("Before: {}".format(arr[1,0]))
view = arr[1]
view[0] += 100
print("After: {}".format(arr[1,0]))

arr.mean(axis=0)

is_greater_one = (arr > 1)
print(is_greater_one.mean())