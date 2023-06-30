season = input()
group_type = input()
pupils_count = int(input())
nights_count = int(input())

sport = ''
price = 0

if season == 'Winter':
    if group_type == 'boys':
        price = nights_count * pupils_count * 9.60
        sport = 'Judo'
    elif group_type == 'girls':
        price = nights_count * pupils_count * 9.60
        sport = 'Gymnastics'
    elif group_type == 'mixed':
        price = nights_count * pupils_count * 10
        sport = 'Ski'
elif season == 'Spring':
    if group_type == 'boys':
        price = nights_count * pupils_count * 7.20
        sport = 'Tennis'
    elif group_type == 'girls':
        price = nights_count * pupils_count * 7.20
        sport = 'Athletics'
    elif group_type == 'mixed':
        price = nights_count * pupils_count * 9.50
        sport = 'Cycling'
elif season == 'Summer':
    if group_type == 'boys':
        price = nights_count * pupils_count * 15
        sport = 'Football'
    elif group_type == 'girls':
        price = nights_count * pupils_count * 15
        sport = 'Volleyball'
    elif group_type == 'mixed':
        price = nights_count * pupils_count * 20
        sport = 'Swimming'

if pupils_count >= 50:
    price *= 0.5
elif 20 <= pupils_count <= 50:
    price *= 0.85
elif 10 <= pupils_count <= 20:
    price *= 0.95
    
print(f'{sport} {price:.2f} lv.')