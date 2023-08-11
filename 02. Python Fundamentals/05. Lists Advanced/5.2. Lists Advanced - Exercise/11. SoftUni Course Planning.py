lessons = input().split(', ')

command = input()

while command != 'course start':
    args = command.split(':')
    action = args[0]
    title = args[1]
    exercise = title + '-Exercise'
    
    if action == 'Add':
        if title not in lessons:
            lessons.append(title)
    elif action == 'Insert':
        index = int(args[2])
        if title not in lessons:
            lessons.insert(index, title)
    elif action == 'Remove':
        if title in lessons:
            lessons.remove(title)
            if exercise in lessons:
                lessons.remove(exercise)
    elif action == 'Swap':
        second_title = args[2]
        exercise_two = second_title + "-Exercise"
        
        if title and second_title in lessons:
            index_1 = lessons.index(title)
            index_2 = lessons.index(second_title)
            
            if exercise in lessons and exercise_two in lessons:
                lessons[index_1], lessons[index_2] = \
                    lessons[index_2], lessons[index_1]
                lessons.remove(exercise)
                lessons.remove(exercise_two)
                lessons.insert(index_2 + 1, exercise)
                lessons.insert(index_1 + 1, exercise_two)
            elif exercise in lessons:
                lessons[index_1], lessons[index_2], = lessons[index_2], lessons[index_1]
                lessons.remove(exercise)
                lessons.insert(index_2 + 1, exercise)
            elif exercise_two in lessons:
                lessons[index_1], lessons[index_2] = lessons[index_2], lessons[index_1]
                lessons.remove(exercise_two)
                lessons.insert(index_1 + 1, exercise_two)
            else:
                lessons[index_1], lessons[index_2] = lessons[index_2], lessons[index_1]
    elif action == "Exercise":
        if title not in lessons:
            if exercise not in lessons:
                lessons.append(title)
                lessons.append(exercise)
        else:
            if exercise not in lessons:
                index_1 = lessons.index(title)
                lessons.insert(index_1 + 1, exercise)
                
    command = input()
    
for index, value in enumerate(lessons):
    print(f"{index + 1}.{value}")
        