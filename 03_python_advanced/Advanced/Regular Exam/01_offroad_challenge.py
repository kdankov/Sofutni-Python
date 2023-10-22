from collections import deque

initial_fuel = [int(x) for x in input().split()]
additional_consumption_index = deque([int(x) for x in input().split()])
fuel_needed = deque([int(x) for x in input().split()])

altitudes = []
altitudes_count = 0

while initial_fuel and additional_consumption_index and fuel_needed:
    current_fuel_quantity = initial_fuel.pop()
    current_consumption_index = additional_consumption_index.popleft()
    current_fuel_needed = fuel_needed.popleft()

    result = current_fuel_quantity - current_consumption_index
    if result >= current_fuel_needed:
        altitudes_count += 1
        altitudes.append(f'Altitude {altitudes_count}')
        print(f'John has reached: Altitude {altitudes_count}')
    elif result < current_fuel_needed:
        print(f'John did not reach: Altitude {altitudes_count + 1}')
        break


if 1 <= altitudes_count < 4:
    print(f'John failed to reach the top.')
    print(f'Reached altitudes: {", ".join(x for x in altitudes)}')
elif altitudes_count == 0:
    print(f'John failed to reach the top.')
    print(f'John didn\'t reach any altitude.')
elif altitudes_count == 4:
    print(f'John has reached all the altitudes and managed to reach the top!')



