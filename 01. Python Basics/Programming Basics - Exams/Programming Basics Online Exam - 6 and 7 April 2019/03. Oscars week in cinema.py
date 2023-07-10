movie = input()
hall_type = input()
tickets_bought = int(input())

total_sum = 0

if movie == 'A Star Is Born':
    if hall_type == 'normal':
        total_sum = 7.50 * tickets_bought
    elif hall_type == 'luxury':
        total_sum = 10.50 * tickets_bought
    elif hall_type == 'ultra luxury':
        total_sum = 13.50 * tickets_bought
elif movie == 'Bohemian Rhapsody':
    if hall_type == 'normal':
        total_sum = 7.35 * tickets_bought
    elif hall_type == 'luxury':
        total_sum = 9.45 * tickets_bought
    elif hall_type == 'ultra luxury':
        total_sum = 12.75 * tickets_bought
elif movie == 'Green Book':
    if hall_type == 'normal':
        total_sum = 8.15 * tickets_bought
    elif hall_type == 'luxury':
        total_sum = 10.25 * tickets_bought
    elif hall_type == 'ultra luxury':
        total_sum = 13.25 * tickets_bought
elif movie == 'The Favourite':
    if hall_type == 'normal':
        total_sum = 8.75 * tickets_bought
    elif hall_type == 'luxury':
        total_sum = 11.55 * tickets_bought
    elif hall_type == 'ultra luxury':
        total_sum = 13.95 * tickets_bought
        
print(f'{movie} -> {total_sum:.2f} lv.')