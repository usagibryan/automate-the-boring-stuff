import re

def is_password_strong(password):
    # check if password is at least 8 characters long
    if len(password) < 8:
        return False
    
    # check if password contains at least one uppercase letter
    uppercase_regex = re.compile(r'[A-Z]')
    if not uppercase_regex.search(password):
        return False
    
    # check if password contains at least one lowercase letter
    lowercase_regex = re.compile(r'[a-z]')
    if not lowercase_regex.search(password):
        return False
    
    # check if password contains at least one digit
    digit_regex = re.compile(r'\d')
    if not digit_regex.search(password):
        return False
    
    # if all checks passed, password is strong
    return True

while True:
    user_password = input('Please create a password: ')
    if is_password_strong(user_password):
        print('Password is strong')
        break
    else:
        print('Password is weak. Please try again.')