def distinct_list(numbers):
    unique = []

    for item in numbers:
        if item not in unique:
            unique.append(item)

    return unique


sample_list = [1, 2, 3, 3, 3, 3, 4, 5]

print("Original List:", sample_list)
print("List with distinct elements:", distinct_list(sample_list))