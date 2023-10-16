from collections import deque

times_queue = deque([int(x) for x in input().split()])
tasks = [int(x) for x in input().split()]

ducks_dict = {
    'Darth Vader Ducky': 0,
    'Thor Ducky': 0,
    'Big Blue Rubber Ducky': 0,
    'Small Yellow Rubber Ducky': 0
}

while times_queue and tasks:
    current_time = times_queue.popleft()
    current_task = tasks.pop()

    result = current_time * current_task
    if result <= 60:
        ducks_dict['Darth Vader Ducky'] += 1
    elif result <= 120:
        ducks_dict['Thor Ducky'] += 1
    elif result <= 180:
        ducks_dict['Big Blue Rubber Ducky'] += 1
    elif result <= 240:
        ducks_dict['Small Yellow Rubber Ducky'] += 1
    else:
        tasks.append(current_task - 2)
        times_queue.append(current_time)

print('Congratulations, all tasks have been completed! Rubber ducks rewarded:')

for key, value in ducks_dict.items():
    print(f'{key}: {value}')