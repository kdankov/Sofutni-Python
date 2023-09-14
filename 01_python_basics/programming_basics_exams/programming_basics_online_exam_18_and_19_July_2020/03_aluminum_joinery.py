joineries_count = int(input())
joineries_type = input()
delivery_type = input()

price = 0

is_invalid_order = False

if joineries_type == '90X130':
    price = joineries_count * 110
    
    if joineries_count > 60:
        price *= 0.92
    elif joineries_count > 30:
        price *= 0.95
elif joineries_type == '100X150':
    price = joineries_count * 140
    
    if joineries_count > 80:
        price *= 0.9
    elif joineries_count > 40:
        price *= 0.94
elif joineries_type == '130X180':
    price = joineries_count * 190
    
    if joineries_count > 50:
        price *= 0.88
    elif joineries_count > 20:
        price *= 0.93
elif joineries_type == '200X300':
    price = joineries_count * 250
    
    if joineries_count > 50:
        price *= 0.86
    elif joineries_count > 25:
        price *= 0.91
    
if delivery_type == 'With delivery':
    price += 60

if joineries_count > 99:
    price *= 0.96
elif joineries_count < 10:
    is_invalid_order = True

    
if not is_invalid_order:
    print(f'{price:.2f} BGN')
else:
    print('Invalid order')