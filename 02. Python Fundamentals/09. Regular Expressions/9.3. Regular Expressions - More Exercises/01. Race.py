import re

participants_list = input().split(', ')

name_pattern = r'[a-zA-Z]+'
digits_pattern = r'\d'

participants_dict = {}

current_participant = input()

while current_participant != 'end of race':
    name = re.findall(name_pattern, current_participant)
    distance = re.findall(digits_pattern, current_participant)
    
    decrypted_name = ''.join(name)
    decrypted_distance = 0
    
    for el in distance:
        decrypted_distance += int(el)
    
    if decrypted_name in participants_list:
        if decrypted_name not in participants_dict:
            participants_dict[decrypted_name] = 0
        participants_dict[decrypted_name] += decrypted_distance
    
    current_participant = input()
    
participants_dict = dict(sorted(participants_dict.items(), key = lambda x:x[1], reverse = True))

print(f'1st place: {list(participants_dict.keys())[0]}')
print(f'2nd place: {list(participants_dict.keys())[1]}')
print(f'3rd place: {list(participants_dict.keys())[2]}')