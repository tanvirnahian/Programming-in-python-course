import pandas as pd


data = pd.read_csv(r"C:\Users\User\Desktop\Lab task 8.9\Lab 8\titanic.csv")


print("First 5 rows:")
print(data.head())


print("\nLast 5 rows:")
print(data.tail())


print("\nDataset Information:")
data.info()