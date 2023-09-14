current_line = input()

courses_dict = {}

while current_line != 'end':
    args = current_line.split(' : ')
    course = args[0]
    name = args[1]
    
    if course not in courses_dict:
        courses_dict[course] = []
    
    courses_dict[course].append(name)    
    
    current_line = input()
    
for key, value in courses_dict.items():
    print(f'{key}: {len(value)}')
    for i in range(len(value)):
        print(f'-- {value[i]}')