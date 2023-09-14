n = int(input())

average_score = 0
grades_count = 0

assesment = input()

while assesment != 'Finish':
    current_average = 0
    
    for i in range(1, n + 1):
        current_grade = float(input())
        current_average += current_grade
        average_score += current_grade
        grades_count += 1
        
    current_average /= n
    
    print(f'{assesment} - {current_average:.2f}.')
    
    assesment = input()
    
average_score /= grades_count

print(f'Student\'s final assessment is {average_score:.2f}.')