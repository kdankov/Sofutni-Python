championship_stage = input()
ticket_type = input()
tickets_count = int(input())
photo_with_trophey = input()

has_free_photos = False

price = 0

if championship_stage == 'Quarter final':
    if ticket_type == 'Standard':
        price = tickets_count * 55.50
    elif ticket_type == 'Premium':
        price = tickets_count * 105.20
    elif ticket_type == 'VIP':
        price = tickets_count * 118.90
elif championship_stage == 'Semi final':
    if ticket_type == 'Standard':
        price = tickets_count * 75.88
    elif ticket_type == 'Premium':
        price = tickets_count * 125.22
    elif ticket_type == 'VIP':
        price = tickets_count * 300.40
elif championship_stage == 'Final':
    if ticket_type == 'Standard':
        price = tickets_count * 110.10
    elif ticket_type == 'Premium':
        price = tickets_count * 160.66
    elif ticket_type == 'VIP':
        price = tickets_count * 400

if price > 4000:
    price *= 0.75
    has_free_photos = True
elif price > 2500:
    price *= 0.9
    
if photo_with_trophey == 'Y' and not has_free_photos:
    price += tickets_count * 40
    
print(f'{price:.2f}')