n = int(input())

people_dict = {}

for i in range(n):
    current_line = input().split()
    command = current_line[0]
    username = current_line[1]
    
    if command == 'register':
        license_plate_number = current_line[2]
        if username not in people_dict:
            people_dict[username] = license_plate_number
            print(f'{username} registered {license_plate_number} successfully')
        else:
            print(f'ERROR: already registered with plate number {people_dict[username]}')
    
    elif command == 'unregister':
        if username not in people_dict:
            print(f'ERROR: user {username} not found')
        else:
            people_dict.pop(username)
            print(f'{username} unregistered successfully')

[print(f'{key} => {value}') for key, value in people_dict.items()]
