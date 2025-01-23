import re

def is_valid_password(password):
    # Check length
    if len(password) < 8:
        return False
    # Check for uppercase and lowercase letters
    if not re.search(r'[A-Z]', password) or not re.search(r'[a-z]', password):
        return False
    # Check for at least one number
    if not re.search(r'\d', password):
        return False
    # Check for at least one special character
    if not re.search(r'[!@#$%^&*]', password):
        return False
    return True

# Example usage
password = 'P@ssw0rd'
print(is_valid_password(password))  # Output: True


'''In this program:

Check length: Ensures the password is at least 8 characters long.

Check for uppercase and lowercase letters: Uses regular expressions to ensure the password contains both uppercase ([A-Z]) and lowercase ([a-z]) letters.

Check for at least one number: Uses a regular expression to check for the presence of digits (\d).

Check for at least one special character: Uses a regular expression to check for the presence of special characters ([!@#$%^&*]).

The is_valid_password function returns True if the password meets all the criteria and False otherwise.'''