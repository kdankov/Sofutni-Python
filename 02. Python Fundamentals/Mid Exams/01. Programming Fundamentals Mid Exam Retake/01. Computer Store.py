customer_type = input()

price_without_taxes = 0

while customer_type != 'special' and customer_type != 'regular':
    parts_price = float(customer_type)
    
    if parts_price <= 0:
        print('Invalid price!')
        customer_type = input()
        continue
    
    price_without_taxes += parts_price
    
    customer_type = input()


if price_without_taxes == 0:
    print('Invalid order!')
    exit()
    
taxes = price_without_taxes * 0.2
total_price = price_without_taxes + taxes

if customer_type == 'special':
    total_price *= 0.9

print('Congratulations you\'ve just bought a new computer!')
print(f'Price without taxes: {price_without_taxes:.2f}$')
print(f'Taxes: {taxes:.2f}$')
print('-----------')
print(f'Total price: {total_price:.2f}$')
