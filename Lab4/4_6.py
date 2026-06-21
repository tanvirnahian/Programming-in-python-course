
starts_with = lambda string, sub: string.startswith(sub)


text = "Python Programming"
substring = "Python"

if starts_with(text, substring):
    print("The string starts with the given substring.")
else:
    print("The string does not start with the given substring.")