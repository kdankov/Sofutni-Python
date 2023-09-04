add_cities = input()

cities_dict = {}

while add_cities != 'Sail':
    tokens = add_cities.split('||')
    city = tokens[0]
    population = int(tokens[1])
    gold = int(tokens[2])
    
    if city not in cities_dict:
        cities_dict[city] = {'POPULATION': population, 'GOLD': gold}
    else:
        cities_dict[city]['POPULATION'] += population
        cities_dict[city]['GOLD'] += gold
    
    add_cities = input()

current_line = input()

while current_line != 'End':
    tokens = current_line.split('=>')
    command = tokens[0]
    town = tokens[1]
    
    if command == 'Plunder':
        people = int(tokens[2])
        gold = int(tokens[3])
        
        cities_dict[town]['POPULATION'] -= people
        cities_dict[town]['GOLD'] -= gold
        
        print(f'{town} plundered! {gold} gold stolen, {people} citizens killed.')
        
        if cities_dict[town]['POPULATION'] <= 0 or cities_dict[town]['GOLD'] <= 0:
            del cities_dict[town]
            print(f'{town} has been wiped off the map!')
        
    elif command == 'Prosper':
        gold = int(tokens[2])
        
        if gold < 0:
            print('Gold added cannot be a negative number!')
        else:
            cities_dict[town]['GOLD'] += gold
            print(f'{gold} gold added to the city treasury. {town} now has {cities_dict[town]["GOLD"]} gold.')
        
    
    current_line = input()
    
if len(cities_dict) > 0:
    print(f'Ahoy, Captain! There are {len(cities_dict)} wealthy settlements to go to:')

    for k, v in cities_dict.items():
        print(f'{k} -> Population: {v["POPULATION"]} citizens, Gold: {v["GOLD"]} kg')
else:
    print('Ahoy, Captain! All targets have been plundered and destroyed!')