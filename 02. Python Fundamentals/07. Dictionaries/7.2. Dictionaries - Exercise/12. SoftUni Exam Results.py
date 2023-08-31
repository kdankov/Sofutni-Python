from collections import defaultdict

current_line = input()

students_dict = {}
languages = defaultdict(int)

while current_line != 'exam finished':
    args = current_line.split('-')
    username = args[0]
    
    if 'banned' not in current_line:
        language = args[1]
        points = int(args[2])
        
        if username not in students_dict:
            students_dict[username] = {}
            
        if language not in students_dict[username]:
            students_dict[username][language] = []
        
        students_dict[username][language].append(points)
        languages[language] += 1
    else:
        if username in students_dict:
            students_dict.pop(username)

    current_line = input()
    
print('Results:')

for k, v in students_dict.items():
    for key, value in v.items():
        print(f'{k} | {max(value)}')

print('Submissions:')

[print(f'{key} - {value}') for key, value in languages.items()]