students = int(input())

top_students = 0
average_students = 0
below_average_students = 0
failed_students = 0

average_grade = 0

for i in range(students):
    current_grade = float(input())
    average_grade += current_grade
    
    if current_grade < 3.00:
        failed_students += 1
    elif current_grade <= 3.99:
        below_average_students += 1
    elif current_grade <= 4.99:
        average_students += 1
    else:
        top_students += 1
        
top_students = top_students * 100 / students
average_students = average_students * 100 / students
below_average_students = below_average_students * 100 / students
failed_students = failed_students * 100 / students

average_grade /= students

print(f'Top students: {top_students:.2f}%')
print(f'Between 4.00 and 4.99: {average_students:.2f}%')
print(f'Between 3.00 and 3.99: {below_average_students:.2f}%')
print(f'Fail: {failed_students:.2f}%')
print(f'Average: {average_grade:.2f}')