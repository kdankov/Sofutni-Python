from collections import deque

chocolates = [int(x) for x in input().split(', ')]
cups_of_milk = deque([int(x) for x in input().split(', ')])

milkshakes_count = 0

while milkshakes_count < 5 and len(chocolates) > 0 and len(cups_of_milk) > 0:
    if chocolates[-1] <= 0 or cups_of_milk[0] <= 0:
        if chocolates[-1] <= 0:
            chocolates.pop()

        if cups_of_milk[0] <= 0:
            cups_of_milk.popleft()

        continue

    current_chocolate = chocolates[-1]
    current_cup = cups_of_milk.popleft()

    if current_chocolate == current_cup:
        chocolates.pop()
        milkshakes_count += 1
    else:
        cups_of_milk.append(current_cup)
        chocolates[-1] -= 5

if milkshakes_count == 5:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')

print(f'Chocolate: {", ".join([str(x) for x in chocolates]) if chocolates else "empty"}')

print(f'Milk: {", ".join([str(x) for x in cups_of_milk]) if cups_of_milk else "empty"}')
