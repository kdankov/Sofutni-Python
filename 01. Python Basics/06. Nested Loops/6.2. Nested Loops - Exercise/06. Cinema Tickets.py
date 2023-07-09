movie = input()

students_average = 0
standards_average = 0
kids_average = 0

tickets_count = 0

while movie != 'Finish':
    seats = int(input())
    ticket_type = input()
    
    current_movie_occupation = 0
    
    while ticket_type != 'End':
        if ticket_type == 'student':
            students_average += 1
        elif ticket_type == 'standard':
            standards_average += 1
        elif ticket_type == 'kid':
            kids_average += 1
        
        current_movie_occupation += 1
        tickets_count += 1
        
        if current_movie_occupation == seats:
            break
        
        ticket_type = input()
    
    current_movie_occupation  = current_movie_occupation * 100 / seats
    print(f'{movie} - {current_movie_occupation:.2f}% full.')
    
    movie = input()
    
students_average = students_average * 100 / tickets_count
standards_average = standards_average * 100 / tickets_count
kids_average = kids_average * 100 / tickets_count

print(f'Total tickets: {tickets_count}')
print(f'{students_average:.2f}% student tickets.')
print(f'{standards_average:.2f}% standard tickets.')
print(f'{kids_average:.2f}% kids tickets.')