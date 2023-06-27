days = int(input())
room_type = input()
grade = input()

nights = days - 1
price = 0

if room_type == 'room for one person':
    price = nights * 18
elif room_type == 'apartment':
    price = nights * 25
    
    if nights < 10:
        price *= 0.7
    elif 10 <= nights <= 15:
        price *= 0.65
    else:
        price *= 0.5
elif room_type == 'president apartment':
    price = nights * 35
    
    if nights < 10:
        price *= 0.9
    elif 10 <= nights <= 15:
        price *= 0.85
    else:
        price *= 0.8

price *= 1.25 if grade == 'positive' else 0.9

print(f'{price:.2f}')