import re

def password_strength(password):
    strength = 0

    # Check for minimum length
    if len(list(filter(lambda x: x != ' ', password))) < 8:
        return strength
    else:
        strength += 1

    # Check for presence of uppercase letters
    if re.search('[A-Z]', ''.join(filter(str.isupper, password))):
        strength += 1

    # Check for presence of lowercase letters
    if re.search('[a-z]', ''.join(filter(str.islower, password))):
        strength += 1

    # Check for presence of digits
    if re.search('[0-9]', ''.join(filter(str.isdigit, password))):
        strength += 1

    # Check for presence of special characters
    if re.search('[_@$]', ''.join(filter(lambda x: x in '_@$', password))):
        strength += 1

    return strength

password = input("Enter your password: ")
print("Your password strength is", password_strength(password))