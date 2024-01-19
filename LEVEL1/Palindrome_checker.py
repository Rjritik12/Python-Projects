def is_palindrome(text):  # check if a string is a palindrome
    text = text.lower()  # convert to lowercase
    text = ''.join(char for char in text if char.isalnum())  # remove non-alphanumeric characters
    return text == text[::-1]  # check if string is the same forwards and backwards

# get user input
text = input("Enter a text: ")
if is_palindrome(text):
    print(f"{text} is a palindrome")
else:
    print(f"{text} is not a palindrome")