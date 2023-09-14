moves_count = int(input())

from_0_to_9 = 0
from_10_to_19 = 0
from_20_to_29 = 0
from_30_to_39 = 0
from_40_to_50 = 0
invalid_numbers = 0

total_points = 0

for i in range(moves_count):
    current_points = int(input())
    
    if 0 <= current_points <= 9:
        from_0_to_9 += 1
        total_points += current_points * 0.2
    elif 10 <= current_points <= 19:
        from_10_to_19 += 1
        total_points += current_points * 0.3
    elif 20 <= current_points <= 29:
        from_20_to_29 += 1
        total_points += current_points * 0.4
    elif 30 <= current_points <= 39:
        from_30_to_39 += 1
        total_points += 50
    elif 40 <= current_points <= 50:
        from_40_to_50 += 1
        total_points += 100
    else:
        invalid_numbers += 1
        total_points /= 2
        
from_0_to_9 = from_0_to_9 * 100 / moves_count
from_10_to_19 = from_10_to_19 * 100 / moves_count
from_20_to_29 = from_20_to_29 * 100 / moves_count
from_30_to_39 = from_30_to_39 * 100 / moves_count
from_40_to_50 = from_40_to_50 * 100 / moves_count
invalid_numbers = invalid_numbers * 100 / moves_count

print(f'{total_points:.2f}')
print(f'From 0 to 9: {from_0_to_9:.2f}%')
print(f'From 10 to 19: {from_10_to_19:.2f}%')
print(f'From 20 to 29: {from_20_to_29:.2f}%')
print(f'From 30 to 39: {from_30_to_39:.2f}%')
print(f'From 40 to 50: {from_40_to_50:.2f}%')
print(f'Invalid numbers: {invalid_numbers:.2f}%')