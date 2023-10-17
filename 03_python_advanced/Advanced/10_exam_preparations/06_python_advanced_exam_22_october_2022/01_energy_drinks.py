from collections import deque

caffeine = [int(x) for x in input().split(', ')]
energy_drinks = deque([int(x) for x in input().split(', ')])

MAXIMUM_CAFFEINE_PER_DAY = 300

caffeine_intake = 0

while caffeine and energy_drinks:
    current_caffeine = caffeine.pop()
    current_energy_drink = energy_drinks.popleft()
    result = current_caffeine * current_energy_drink

    if caffeine_intake + result <= 300:
        caffeine_intake += result
    else:
        energy_drinks.append(current_energy_drink)
        caffeine_intake = caffeine_intake - 30 if caffeine_intake - 30 >= 0 else 0

if energy_drinks:
    print(f'Drinks left: {", ".join([str(x) for x in energy_drinks])}')
else:
    print('At least Stamat wasn\'t exceeding the maximum caffeine.')

print(f'Stamat is going to sleep with {caffeine_intake} mg caffeine.')
