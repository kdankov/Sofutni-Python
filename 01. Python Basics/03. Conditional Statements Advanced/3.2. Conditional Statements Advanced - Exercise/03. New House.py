flowers_type = input()
count = int(input())
budget = int(input())

price = 0

if flowers_type == 'Roses':
    price = 5 * count
    if count > 80:
        price *= 0.9
elif flowers_type == 'Dahlias':
    price = 3.80 * count
    if count > 90:
        price *= 0.85
elif flowers_type == 'Tulips':
    price = 2.80 * count
    if count > 80:
        price *= 0.85
elif flowers_type == 'Narcissus':
    price = 3 * count
    if count < 120:
        price *= 1.15
elif flowers_type == 'Gladiolus':
    price = 2.50 * count
    if count < 80:
        price *= 1.2

if price <= budget:
    print(f'Hey, you have a great garden with {count} {flowers_type} and {budget - price:.2f} leva left.')
else:
    print(f'Not enough money, you need {price - budget:.2f} leva more.')
