import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}


myseries = pd.Series(calories)


total = myseries.sum()

print("Calories:")
print(myseries)

print("Total calories =", total)