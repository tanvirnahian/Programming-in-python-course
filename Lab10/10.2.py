import numpy as np

arr = np.array([10, 20, 30, 40, 50])

value = 30

position = np.where(arr == value)

print("Position of", value, ":", position)