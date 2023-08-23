elements = [int(x) for x in input().split()]

command = input()

while command != 'end':
    args = command.split()
    action = args[0]
    
    if action == 'swap':
        index1 = int(args[1])
        index2 = int(args[2])
        elements[index1], elements[index2] = elements[index2], elements[index1]
    elif action == 'multiply':
        index1 = int(args[1])
        index2 = int(args[2])
        elements[index1] *= elements[index2]
    elif action == 'decrease':
        elements = [el - 1 for el in elements]
    
    command = input()
    
print(', '.join([str(x) for x in elements]))
    