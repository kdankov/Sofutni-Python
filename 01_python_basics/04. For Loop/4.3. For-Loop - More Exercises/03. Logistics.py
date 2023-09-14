loads_count = int(input())

microbus_average = 0
truck_average = 0
train_average = 0

total_weight = 0

for i in range(loads_count):
    current_weight = int(input())
    total_weight += current_weight
    
    if current_weight <= 3:
        microbus_average += current_weight
    elif current_weight <= 11:
        truck_average += current_weight
    else:
        train_average += current_weight
        
average_price_per_ton = (microbus_average * 200 + truck_average * 175 + train_average * 120) / total_weight

microbus_average = microbus_average / total_weight * 100
truck_average = truck_average / total_weight * 100
train_average = train_average / total_weight * 100

print(f'{average_price_per_ton:.2f}')
print(f'{microbus_average:.2f}%')
print(f'{truck_average:.2f}%')
print(f'{train_average:.2f}%')
