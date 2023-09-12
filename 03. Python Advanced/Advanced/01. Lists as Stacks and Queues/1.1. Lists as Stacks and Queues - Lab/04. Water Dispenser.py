from collections import deque

water_quantity = int(input())
name = input()

water_queue = deque()

while name != 'Start':
    water_queue.append(name)

    name = input()

command = input()

while command != 'End':
    data = command.split()

    if len(data) == 1:
        liters_to_give = int(data[0])
        person = water_queue.popleft()
        if liters_to_give <= water_quantity:
            print(f'{person} got water')
            water_quantity -= liters_to_give
        else:
            print(f'{person} must wait')
    else:
        liters_to_add = int(data[1])
        water_quantity += liters_to_add

    command = input()

print(f'{water_quantity} liters left')
