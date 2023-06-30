budget = float(input())
category = input()
people_count = int(input())

price = 0

if 1 <= people_count <= 4:
    budget *= 0.25
elif people_count <= 9:
    budget *= 0.4
elif people_count <= 24:
    budget *= 0.5
elif people_count <= 49:
    budget *= 0.6
else:
    budget *= 0.75

if category == 'VIP':
    price = 499.99 * people_count
elif category == 'Normal':
    price = 249.99 * people_count
    

if price <= budget:
    print(f'Yes! You have {budget - price:.2f} leva left.')
else:
    print(f'Not enough money! You need {price - budget:.2f} leva.')
    