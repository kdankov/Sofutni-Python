from collections import defaultdict

products = defaultdict(int)

command = input()

while command != 'statistics':
    product, quantity = command.split(': ')
    products[product] += int(quantity)
    
    command = input()
    
print('Products in stock:')

# for (product, quantity) in products.items():
#     print(f'- {product}: {quantity}')

[print(f'- {product}: {quantity}') for product, quantity in products.items()]

print(f'Total Products: {len(products.keys())}')
print(f'Total Quantity: {sum(products.values())}')

