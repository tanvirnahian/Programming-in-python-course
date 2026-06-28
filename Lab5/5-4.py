

numbers = [12, 45, 7, 23, 89, 34]

target = int(input("Enter the number to search: "))

found = False

for i in range(len(numbers)):
    if numbers[i] == target:
        print("Number found at index", i)
        found = True
        break

if found == False:
    print("Number not found.")