# Find the maximum and minimum values in a list

numbers = [12, 45, 7, 23, 89, 34]

maximum = numbers[0]
minimum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num

print("List:", numbers)
print("Maximum value:", maximum)
print("Minimum value:", minimum)