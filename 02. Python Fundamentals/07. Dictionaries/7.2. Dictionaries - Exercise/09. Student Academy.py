n = int(input())

students_dict = {}

for i in range(n):
    name = input()
    grade = float(input())
    
    if name not in students_dict:
        students_dict[name] = []
    students_dict[name].append(grade)
    
students_dict = dict([(k, v) for k, v in students_dict.items() if sum(v) / len(v) >= 4.50])
        
[print(f'{key} -> {sum(value) / len(value):.2f}') for key, value in students_dict.items()]