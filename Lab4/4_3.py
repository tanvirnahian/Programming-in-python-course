def is_palindrome(text):
    if text == text[::-1]:
        return True
    else:
        return False


word = input("Enter a string: ")

if is_palindrome(word):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")