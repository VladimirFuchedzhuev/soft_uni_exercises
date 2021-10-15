def password_validator_length(password):
    if 6<= len(password) <= 10:
        return True

    return False

def password_alphanumeric(password):
    if password.isalnum():
        return True

    return False

def two_digits_password(password):
    digits = [ch for ch in password if ch.isdigit()]
    if len(digits) >= 2:
        return True

    return False

def password_validation(password):
    is_valid = True

    if not password_validator_length(password):
        print("Password must be between 6 and 10 characters")
        is_valid = False

    if not password_alphanumeric(password):
        print("Password must consist only of letters and digits")
        is_valid = False

    if not two_digits_password(password):
        print("Password must have at least 2 digits")
        is_valid = False

    if is_valid:
        print("Password is valid")
        
        
password_input = input()

password_validation(password_input)