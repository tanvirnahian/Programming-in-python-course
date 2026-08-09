import pandas as pd

data = pd.read_csv(r"C:\Users\User\Desktop\Lab task 8.9\Lab 8\titanic.csv")

print("Original Data:")
print(data.head())


print("\nEmpty cells:")
print(data.isnull().sum())

data = data.dropna()


data = data.drop_duplicates()


if "Age" in data.columns:
    data["Age"] = pd.to_numeric(data["Age"], errors="coerce")


if "Age" in data.columns:
    data = data.dropna(subset=["Age"])


print("\nCleaned Data:")
print(data.head())


print("\nInformation after cleaning:")
data.info()