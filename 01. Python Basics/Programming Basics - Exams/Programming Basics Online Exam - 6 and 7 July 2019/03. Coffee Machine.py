drink = input()
sugar = input()
quantity = int(input())

price = 0

if drink == 'Espresso':
    if sugar == 'Without':
        price = (0.9 * quantity) * 0.65
    elif sugar == 'Normal':
        price = 1 * quantity
    elif sugar == 'Extra':
        price = 1.20 * quantity
    
    if quantity >= 5:
            price *= 0.75
elif drink == 'Cappuccino':
    if sugar == 'Without':
        price = (1 * quantity) * 0.65
    elif sugar == 'Normal':
        price = 1.20 * quantity
    elif sugar == 'Extra':
        price = 1.6 * quantity
elif drink == 'Tea':
    if sugar == 'Without':
        price = (0.5 * quantity) * 0.65
    elif sugar == 'Normal':
        price = 0.6 * quantity
    elif sugar == 'Extra':
        price = 0.7 * quantity
        
if price > 15:
    price *= 0.8
    
print(f'You bought {quantity} cups of {drink} for {price:.2f} lv.')
        