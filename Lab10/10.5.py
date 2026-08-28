import numpy as np

arr = np.array([5, -2, 8, -7, 3, -1])

arr[arr < 0] = 0

print("Array after replacing negative values:")
print(arr)