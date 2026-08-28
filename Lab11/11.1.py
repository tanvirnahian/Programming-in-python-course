import numpy as np

arr = np.array([8, 3, 6, 1, 9, 2, 5])

k = 3

smallest = np.sort(arr)[:k]

print("K-smallest values:", smallest)