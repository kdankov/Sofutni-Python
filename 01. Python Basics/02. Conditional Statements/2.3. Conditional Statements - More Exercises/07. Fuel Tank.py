fuel_type = input()
litres = float(input())

types_of_fuel = ['Diesel', 'Gasoline', 'Gas']

if fuel_type not in types_of_fuel:
    print('Invalid fuel!')
else:
    if litres >= 25:
        print(f'You have enough {fuel_type.lower()}.')
    else:
        print(f'Fill your tank with {fuel_type.lower()}!')
    
