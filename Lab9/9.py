import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv(
    r"C:\Users\User\Desktop\Lab task 8.9\Lab 8\titanic.csv"
)

print("First 5 rows:")
print(data.head())

print("\nColumn names:")
print(data.columns)



plt.figure(figsize=(8, 5))

plt.plot(data["Age"].head(20))

plt.title("Age of First 20 Passengers")
plt.xlabel("Passenger Number")
plt.ylabel("Age")

plt.show()



plt.figure(figsize=(8, 5))

plt.scatter(data["Age"], data["Fare"])

plt.title("Age vs Fare")
plt.xlabel("Age")
plt.ylabel("Fare")

plt.show()




survived = data["Survived"].value_counts()

plt.figure(figsize=(7, 5))

plt.bar(["Not Survived", "Survived"], survived.values)

plt.title("Number of Survived and Not Survived Passengers")
plt.xlabel("Survival")
plt.ylabel("Number of Passengers")

plt.show()


plt.figure(figsize=(8, 5))

plt.hist(data["Age"].dropna(), bins=10)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")

plt.show()


-

sex_count = data["Sex"].value_counts()

plt.figure(figsize=(7, 7))

plt.pie(
    sex_count.values,
    labels=sex_count.index,
    autopct="%1.1f%%"
)

plt.title("Male and Female Passengers")

plt.show()



fig, axes = plt.subplots(2, 2, figsize=(12, 8))


axes[0, 0].hist(data["Age"].dropna(), bins=10)
axes[0, 0].set_title("Age Distribution")
axes[0, 0].set_xlabel("Age")
axes[0, 0].set_ylabel("Frequency")


axes[0, 1].hist(data["Fare"].dropna(), bins=10)
axes[0, 1].set_title("Fare Distribution")
axes[0, 1].set_xlabel("Fare")
axes[0, 1].set_ylabel("Frequency")



survived = data["Survived"].value_counts()

axes[1, 0].bar(["Not Survived", "Survived"], survived.values)
axes[1, 0].set_title("Survival")



class_count = data["Pclass"].value_counts().sort_index()

axes[1, 1].bar(class_count.index.astype(str), class_count.values)
axes[1, 1].set_title("Passengers by Class")
axes[1, 1].set_xlabel("Class")
axes[1, 1].set_ylabel("Number")

plt.tight_layout()

plt.show()