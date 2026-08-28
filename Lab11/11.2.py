import numpy as np

arr = np.array([10, 20, 10, 30, 10, 40, 10])

item = 10
n = 3

positions = np.where(arr == item)[0]

print("Index of", n, "rd repetition:", positions[n - 1])