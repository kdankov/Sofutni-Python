def is_digit(num):
    return num >= 48 and num <= 57


def num_count_minimum(password):
    return len([x for x in password if x.isdigit()]) >= 2
        

def length_validator(password):
        return 6 <= len(password) <= 10


def is_letter_digit(password):
    return password.isalnum()


password = input()

if length_validator(password) and is_letter_digit(password) and num_count_minimum(password):
    print('Password is valid')
else:
    if not length_validator(password):
        print('Password must be between 6 and 10 characters')
        
    if not is_letter_digit(password):
        print('Password must consist only of letters and digits')

    if not num_count_minimum(password):
        print('Password must have at least 2 digits')