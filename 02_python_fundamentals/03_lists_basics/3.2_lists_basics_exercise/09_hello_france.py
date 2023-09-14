items = input().split('|')
budget = float(input())

ticket_price = 150

bought_items_prices = []
profit = 0

for item in items:
    tokens = item.split('->')
    item_type = tokens[0]
    item_price = float(tokens[1])
    
    is_valid = False
    
    if item_price > budget:
        continue
    
    if item_type == 'Clothes' and item_price <= 50:
        is_valid = True
    elif item_type == 'Shoes' and item_price <= 35:
        is_valid = True
    elif item_type == 'Accessories' and item_price <= 20.50:
        is_valid = True
    
    if is_valid:
        budget -= item_price
        profit += item_price
        bought_items_prices.append(item_price * 1.4)

for item in bought_items_prices:
    print(f'{item:.2f}', end=' ')

print()

profit = sum(bought_items_prices) - profit
print(f'Profit: {profit:.2f}')

if budget + sum(bought_items_prices) >= ticket_price:
    print('Hello, France!')
else:
    print('Not enough money.')