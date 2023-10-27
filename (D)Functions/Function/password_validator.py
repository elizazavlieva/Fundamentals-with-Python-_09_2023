def characters_long(password):
    if 6 <= len(password) <= 10:
        return True
    return False


def letters_and_digits(password):
    return password.isalnum()


def digit_counter(password, digit):
    for i, index in enumerate(password):
        if index.isdigit():
            digit += 1
    if digit > 1:
        return True
    return False


def password_validator(password, digit):
    is_long_enough = characters_long(password)
    is_letter_and_digit = letters_and_digits(password)
    is_more_than_one_digits = digit_counter(password, digit)
    if is_more_than_one_digits and is_letter_and_digit and is_long_enough:
        print('Password is valid')
    if not is_long_enough:
        print('Password must be between 6 and 10 characters')
    if not is_letter_and_digit:
        print('Password must consist only of letters and digits')
    if not is_more_than_one_digits:
        print('Password must have at least 2 digits')


user_input = input()
counter = 0
password_validator(user_input, counter)
