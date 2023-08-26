students = {}

needed_course = ''

while True:
    current_line = input()
    
    if ':' in current_line:
        current_student = current_line.split(':')
        name = current_student[0]
        ID = current_student[1]
        course = current_student[2]
        
        if name not in students:
            students[name] = list()
        students[name].append(ID)
        students[name].append(course)
    else:
        needed_course = current_line
        break

needed_course = needed_course.replace('_', ' ')

[print(f'{name} - {value[0]}') for name, value in students.items() if value[-1] == needed_course]