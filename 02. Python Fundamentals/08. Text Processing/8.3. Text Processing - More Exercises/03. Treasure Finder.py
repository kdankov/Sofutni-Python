key = input().split()

current_line = input()

while current_line != 'find':
    decrypted = ''
    count = 0

    while count < len(current_line):
        for i in range(len(key)):
            if count == len(current_line):
                break

            current_number = int(key[i])
            current_char = ord(current_line[count])
        
            count += 1
            
            decrypted_char = chr(current_char - current_number)
            decrypted += decrypted_char 

    first_index_type = decrypted.index('&')
    last_index_type = decrypted.rindex('&')
    type_treasure = decrypted[first_index_type + 1: last_index_type]
    
    first_index_coordinates = decrypted.index('<')
    last_index_coordinates = decrypted.rindex('>')
    coordinates = decrypted[first_index_coordinates + 1: last_index_coordinates]
    
    print(f'Found {type_treasure} at {coordinates}')
    
    current_line = input()