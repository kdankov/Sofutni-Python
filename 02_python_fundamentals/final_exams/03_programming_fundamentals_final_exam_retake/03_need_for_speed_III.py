n = int(input())

cars_dict = {}

for i in range(n):
    current_car = input().split('|')
    brand = current_car[0]
    mileage = int(current_car[1])
    fuel = int(current_car[2])
    
    if brand not in cars_dict:
        cars_dict[brand] = {'Mileage': mileage, 'Fuel': fuel}
        
current_line = input()

while current_line != 'Stop':
    tokens = current_line.split(' : ')
    operation = tokens[0]
    car = tokens[1]
    
    if operation == 'Drive':
        distance = int(tokens[2])
        fuel = int(tokens[3])
    
        if cars_dict[car]['Fuel'] < fuel:
            print('Not enough fuel to make that ride')
        else:
            cars_dict[car]['Mileage'] += distance
            cars_dict[car]['Fuel'] -= fuel
            print(f'{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.')
        
        if cars_dict[car]['Mileage'] >= 100000:
            del cars_dict[car]
            print(f'Time to sell the {car}!')

    elif operation == 'Refuel':
        fuel = int(tokens[2])
        
        refueled = 0
        
        if cars_dict[car]['Fuel'] + fuel >= 75:
            refueled = 75 - cars_dict[car]['Fuel']
            cars_dict[car]['Fuel'] = 75
        else:
            refueled = fuel
            cars_dict[car]['Fuel'] += fuel
            
        print(f'{car} refueled with {refueled} liters')
    
    elif operation == 'Revert':
        kilometers = int(tokens[2])
        
        cars_dict[car]['Mileage'] -= kilometers
        
        if cars_dict[car]['Mileage'] <= 10000:
            cars_dict[car]['Mileage'] = 10000
        else:
            print(f'{car} mileage decreased by {kilometers} kilometers')

    current_line = input()
    
for k, v in cars_dict.items():
    print(f'{k} -> Mileage: {v["Mileage"]} kms, Fuel in the tank: {v["Fuel"]} lt.')
