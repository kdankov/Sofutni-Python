def is_valid(word):
    if len(word) < 3 or len(word) > 16:
        return False

    for symbol in word:
        if not symbol.isdigit() and not symbol.isalpha() and symbol != '-' and symbol != '_':
            return False
        
    return True

usernames = input().split(', ')

for username in usernames:
    if is_valid(username):
        print(username)