orders_count = int(input())

total_price = 0

for i in range(orders_count):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    
    current_price = 0
    
    if 0.01 > price_per_capsule or price_per_capsule > 100 or 1 > days or days > 31 or 1 > capsules_per_day or capsules_per_day > 2000:
        continue
        
    current_price = price_per_capsule * capsules_per_day * days
    total_price += current_price
    print(f'The price for the coffee is: ${current_price:.2f}')

print(f'Total: ${total_price:.2f}')
