import re

def is_valid_email():
   
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    
    email = input("Please enter your email address: ")

    if re.match(email_regex, email):
        return True
    else:
        return False

result = is_valid_email()
print(result)