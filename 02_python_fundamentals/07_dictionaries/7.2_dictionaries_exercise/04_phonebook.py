from collections import defaultdict

person_data = input()

phonebook = defaultdict(int)

n = 0
while True:
    if '-' in person_data:
        name, number = person_data.split('-')
        phonebook[name] = number
    else:
        n = int(person_data)
        break
    
    person_data = input()
    
for i in range(n):
    current_name = input()
    if current_name in phonebook.keys():
        print(f'{current_name} -> {phonebook[current_name]}')
    else:
        print(f'Contact {current_name} does not exist.')
