numbers = [int(x) for x in input().split(', ')]

current_max = 10

while len(numbers) > 0:
    current_list = [x for x in numbers if x <= current_max]
    numbers = [x for x in numbers if x > current_max]
    
    print(f'Group of {current_max}\'s: {current_list}')
    current_max += 10
