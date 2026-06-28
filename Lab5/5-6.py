
numbers = [10, 20, 30, 20, 50]


unique_list = []


for item in numbers:
    if item not in unique_list:
        unique_list.append(item)

print(unique_list)