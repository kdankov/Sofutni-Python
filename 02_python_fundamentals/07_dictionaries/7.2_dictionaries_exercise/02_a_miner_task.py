from collections import defaultdict

resources = defaultdict(int)

resource = input()

while resource != 'stop':
    quantity = int(input())
    
    resources[resource] += quantity
    
    resource = input()
    
[print(f'{resource} -> {quantity}') for resource, quantity in resources.items()]
