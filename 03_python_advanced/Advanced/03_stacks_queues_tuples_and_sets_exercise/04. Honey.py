from collections import deque

working_bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())

honey = 0

while len(working_bees) > 0 and len(nectar) > 0:
    current_bee = working_bees[0]
    current_nectar = nectar[-1]
    current_symbol = symbols[0]

    if current_nectar >= current_bee:
        if current_symbol == '+':
            honey += abs(current_bee + current_nectar)

        elif current_symbol == '-':
            honey += abs(current_bee - current_nectar)

        elif current_symbol == '*':
            honey += abs(current_bee * current_nectar)

        elif current_symbol == '/':
            if current_nectar == 0:
                working_bees.popleft()
                nectar.pop()
                symbols.popleft()
                continue
            else:
                honey += abs(current_bee / current_nectar)

        working_bees.popleft()
        nectar.pop()
        symbols.popleft()
    else:
        nectar.pop()

print(f'Total honey made: {honey}')

if working_bees:
    print(f'Bees left: {", ".join([str(x) for x in working_bees])}')

if nectar:
    print(f'Nectar left: {", ".join(([str(x) for x in working_bees]))}')