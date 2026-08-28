import pandas as pd

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}


df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)


print("\nSelected rows:")
print(df.loc[[0, 2]])