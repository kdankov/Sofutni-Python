from sys import maxsize
numbers = [int(x) for x in input().split()]

command = input()

while command != 'end':
    args = command.split()
    action = args[0]
    
    if action == 'exchange':
        index = int(args[1])
        
        if 0 <= index < len(numbers):
            for i in range(index + 1):
                numbers.append(numbers.pop(0))
        else:
            print('Invalid index')
    elif action == 'max':
        even_or_odd = args[1]
        
        current_max = -maxsize
        max_index = 0
        
        for index, value in enumerate(numbers):
            if value >= current_max and value % 2 == 0 and even_or_odd == 'even':
                current_max = value
                max_index = index
            elif value >= current_max and value % 2 != 0 and even_or_odd == 'odd':
                current_max = value
                max_index = index
                
        if current_max == -maxsize:
            print('No matches')
        else:
            print(max_index)
    elif action == 'min':
        even_or_odd = args[1]
        
        current_min = maxsize
        min_index = 0
        
        for index, value in enumerate(numbers):
            if value <= current_min and value % 2 == 0 and even_or_odd == 'even':
                current_min = value
                min_index = index
            elif value <= current_min and value % 2 != 0 and even_or_odd == 'odd':
                current_min = value
                min_index = index
        
        if current_min == maxsize:
            print('No matches')
        else:
            print(min_index)
    elif action == 'first' or action == 'last':
        count = int(args[1])
        even_or_odd = (args[2])
        
        if count > len(numbers):
            print('Invalid count')
            command = input()
            continue
        
        result = []
        
        for index, value in enumerate(numbers):
            if value % 2 == 0 and even_or_odd == 'even':
                result.append(value)
            elif value % 2 != 0 and even_or_odd == 'odd':
                result.append(value)
        
        if action == 'first':
            if count > len(result):
                print(result)
            else:
                print(result[:count])
        elif action == 'last':
            if count > len(result):
                print(result)
            else:
                print(result[-count:])

    command = input()

print(numbers)
