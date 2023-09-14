numbers = [int(x) for x in input().split(' ')]

left_racer_time = 0
right_racer_time = 0

half = int(len(numbers) / 2)

for i in range(0, half):
    left_racer_time += numbers[i]
    
    if numbers[i] == 0:
        left_racer_time *= 0.8


for i in range(len(numbers) - 1, half, -1):
    right_racer_time += numbers[i]
    
    if numbers[i] == 0:
        right_racer_time *= 0.8

    
if left_racer_time < right_racer_time:
    print(f'The winner is left with total time: {left_racer_time:.1f}')
else:
    print(f'The winner is right with total time: {right_racer_time:.1f}')
