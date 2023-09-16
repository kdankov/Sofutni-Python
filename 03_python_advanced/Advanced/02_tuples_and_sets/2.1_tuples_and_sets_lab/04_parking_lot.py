cars_count = int(input())

parking = set()

for _ in range(cars_count):
    direction, number = input().split(', ')

    if direction == 'IN':
        parking.add(number)

    elif direction == 'OUT':
        parking.remove(number)

if len(parking) > 0:
    for car in parking:
        print(car)
else:
    print('Parking Lot is Empty')
