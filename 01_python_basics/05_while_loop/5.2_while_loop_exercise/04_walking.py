goal = 10000

total_steps = 0

while total_steps < goal:
    current_steps = input()
    
    if current_steps == 'Going home':
        current_steps = int(input())
        total_steps += int(current_steps)
        break
    
    total_steps += int(current_steps)

if total_steps >= goal:
    print('Goal reached! Good job!')
    print(f'{total_steps - goal} steps over the goal!')
else:
    print(f'{goal - total_steps} more steps to reach goal.')