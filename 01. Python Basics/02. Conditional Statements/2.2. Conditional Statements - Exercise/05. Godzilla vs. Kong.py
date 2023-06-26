budget = float(input())
extras = int(input())
clothes_price = float(input())

decor_price = budget * 0.1

clothes_price *= extras

if extras > 150:
    clothes_price *= 0.90
    
price = decor_price + clothes_price

if price <= budget:
    print('Action!')
    print(f'Wingard starts filming with {budget - price:.2f} leva left.')
else:
    print('Not enough money!')
    print(f'Wingard needs {price - budget:.2f} leva more.')
    