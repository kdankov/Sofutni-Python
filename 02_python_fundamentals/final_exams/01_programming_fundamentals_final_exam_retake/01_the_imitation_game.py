encrypted_message = input()

current_line = input()

while current_line != 'Decode':
    tokens = current_line.split('|')
    operation = tokens[0]
    
    if operation == 'Move':
        count = int(tokens[1])
        
        removed = encrypted_message[:count]
        encrypted_message = encrypted_message[count:] + removed
            
    elif operation == 'Insert':
        index = int(tokens[1])
        value = tokens[2]
        
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]
    
    elif operation == 'ChangeAll':
        substring = tokens[1]
        replacement = tokens[2]
        
        encrypted_message = encrypted_message.replace(substring, replacement)
    
    current_line = input()
    
print(f'The decrypted message is: {encrypted_message}')