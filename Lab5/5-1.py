

text = "hello .py"

words = text.split()
reversed_words = []

for word in words:
    reversed_words.append(word[::-1])

result = " ".join(reversed_words)

print("Original String:", text)
print("Reversed Words:", result)