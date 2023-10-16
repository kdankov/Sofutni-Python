from collections import deque

textiles_queue = deque([int(x) for x in input().split()])
medicaments = [int(x) for x in input().split()]

items_dict = {'Patch': 0, 'Bandage': 0, 'MedKit': 0}

while textiles_queue and medicaments:
    current_textile = textiles_queue.popleft()
    current_medicament = medicaments.pop()

    resources = current_textile + current_medicament

    if resources == 30:
        items_dict['Patch'] += 1
    elif resources == 40:
        items_dict['Bandage'] += 1
    elif resources >= 100:
        items_dict['MedKit'] += 1

        if resources > 100:
            resources -= 100
            medicaments[-1] += resources
    else:
        current_medicament += 10
        medicaments.append(current_medicament)

sorted_items = sorted(items_dict.items(), key=lambda x: (-x[1], x[0]))

if not textiles_queue and not medicaments:
    print('Textiles and medicaments are both empty.')
else:
    if not textiles_queue:
        print('Textiles are empty.')

    if not medicaments:
        print('Medicaments are empty.')

[print(f'{item} - {amount}') for item, amount in sorted_items if amount > 0]

if medicaments:
    medicaments.reverse()
    print(f'Medicaments left: {", ".join([str(x) for x in medicaments])}')

if textiles_queue:
    print(f'Textiles left: {", ".join([str(x) for x in textiles_queue])}')
