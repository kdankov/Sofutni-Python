first_employee_efficiency = int(input())
second_employee_efficiency = int(input())
third_employee_efficiency = int(input())
students_count = int(input())

total_employee_efficiency = first_employee_efficiency + second_employee_efficiency + third_employee_efficiency
hours = 0

while students_count > 0:
    students_count -= total_employee_efficiency
    hours += 1
    
    if hours % 4 == 0:
        hours += 1
        
print(f'Time needed: {hours}h.')