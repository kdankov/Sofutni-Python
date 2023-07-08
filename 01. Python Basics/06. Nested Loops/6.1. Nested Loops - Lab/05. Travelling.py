destination = input()

current_budget = 0

while destination != 'End':
    needed_budget = float(input())
    
    while current_budget < needed_budget:
        current_sum = float(input())
        current_budget += current_sum
        
    print(f'Going to {destination}!')
    current_budget = 0
    destination = input()
    