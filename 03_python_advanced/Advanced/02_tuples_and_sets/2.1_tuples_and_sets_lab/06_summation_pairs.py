# NOT INCLUDED IN THE JUDGE SYSTEM

numbers = [int(x) for x in input().split()]
target = int(input())

targets = set()
values_map = {}

for value in numbers:
    if value in targets:
        targets.remove(value)
        pair = values_map[value]
        del values_map[value]
        print(f'{pair} + {value} = {target}')
    else:
        resulting_number = target - value
        targets.add(resulting_number)
        values_map[resulting_number] = value
