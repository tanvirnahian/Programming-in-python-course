try:
    file = open("student.txt", "x")
    file.write("Hello! This is the first line.\n")
    file.close()
    print("File created successfully.")

except FileExistsError:
    print("File already exists.")

try:
    # Write
    file = open("student.txt", "w")
    file.write("Welcome to Python File Handling.\n")
    file.close()

    # Append
    file = open("student.txt", "a")
    file.write("This line is added later.\n")
    file.close()

    # Read
    file = open("student.txt", "r")
    print("\nFile Content:")
    print(file.read())
    file.close()

except Exception as e:
    print("An error occurred:", e)