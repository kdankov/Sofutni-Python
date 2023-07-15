clients_count = int(input())

average_price = 0

for i in range(clients_count):
    product = input()
    
    current_price = 0
    current_items_count = 0
    
    while product != 'Finish':
        current_items_count += 1
        if product == 'basket':
            current_price += 1.50
        elif product == 'wreath':
            current_price += 3.80
        elif product == 'chocolate bunny':
            current_price += 7
        
        product = input()
    
    if current_items_count % 2 == 0:
        current_price *= 0.8
        
    print(f'You purchased {current_items_count} items for {current_price:.2f} leva.')
    
    average_price += current_price
    
average_price /= clients_count

print(f'Average bill per client is: {average_price:.2f} leva.')