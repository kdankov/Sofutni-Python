from math import ceil

students_count = int(input())
lectures_count = int(input())
additional_bonus = int(input())

best_student = {
    'max_bonus': 0,
    'attended_lectures': 0
}

for i in range(students_count):
    current_attendances = int(input())
    
    total_bonus = current_attendances / lectures_count * (5 + additional_bonus)
    
    if total_bonus > best_student['max_bonus']:
        best_student['max_bonus'] = total_bonus
        best_student['attended_lectures'] = current_attendances
        
print(f'Max Bonus: {ceil(best_student["max_bonus"])}.')
print(f'The student has attended {best_student["attended_lectures"]} lectures.')
