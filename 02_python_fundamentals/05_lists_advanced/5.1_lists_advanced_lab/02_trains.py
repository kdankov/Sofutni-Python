wagons_count = int(input())

train = [0] * wagons_count

command = input()

while command != 'End':
    args = command.split()
    action = args[0]
    
    if action == 'add':
        people = int(args[1])
        train[-1] += people
    elif action == 'insert':
        index = int(args[1])
        people = int(args[2])
        train[index] += people
    elif action == 'leave':
        index = int(args[1])
        people = int(args[2])
        train[index] -= people
    
    command = input()

print(train)
