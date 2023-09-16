students_count = int(input())

students_dict = {}

for _ in range(students_count):
    name, grade = input().split()

    if name not in students_dict:
        students_dict[name] = []
    students_dict[name].append(float(grade))

for student_name, grades in students_dict.items():
    formatted_grades = ' '.join([f"{grade:.2f}" for grade in grades])
    print(f'{student_name} -> {formatted_grades} (avg: {sum(grades) / len(grades):.2f})')
