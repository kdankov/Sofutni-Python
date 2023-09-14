message = input()

current_line = input()

while current_line != 'Reveal':
    tokens = current_line.split(':|:')
    operation = tokens[0]
    
    if operation == 'InsertSpace':
        index = int(tokens[1])
        
        message = message[:index] + ' ' + message[index:]
        
        print(message)
        
    elif operation == 'Reverse':
        substring = tokens[1]
        
        if substring in message:
            message = message.replace(substring, '', 1)
            substring = substring[::-1]
            message += substring
            
            print(message)
        else:
            print('error')
            
    elif operation == 'ChangeAll':
        substring = tokens[1]
        replacement = tokens[2]
        
        if substring in message:
            message = message.replace(substring, replacement)
            print(message)
    
    current_line = input()
    
print(f'You have a new text message: {message}')