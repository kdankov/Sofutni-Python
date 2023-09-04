password = input()

current_line = input()

while current_line != 'Done':
    tokens = current_line.split()
    command = tokens[0]
    
    if command == 'TakeOdd':
        password = password[1::2]
        
        print(password)
    
    elif command == 'Cut':
        index = int(tokens[1])
        length = int(tokens[2])
        
        password = password[:index] + password[index + length:]
        
        print(password)
    
    elif command == 'Substitute':
        substring = tokens[1]
        substitute = tokens[2]
        
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print('Nothing to replace!')

    current_line = input()

print(f'Your password is: {password}')