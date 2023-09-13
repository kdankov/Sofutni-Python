from collections import deque

cups = deque([int(x) for x in input().split()])
bottles = [int(x) for x in input().split()]

wasted_water = 0

while True:
    if len(bottles) == 0 or len(cups) == 0:
        break

    if bottles[-1] >= cups[0]:
        wasted_water += bottles[-1] - cups[0]
        bottles.pop()
        cups.popleft()
    else:
        cups[0] -= bottles.pop()

        if cups[0] <= 0:
            wasted_water += cups[0]
            cups.popleft()

if cups:
    print(f'Cups:', end=' ')
    while cups:
        print(cups.popleft(), end=' ')
else:
    print(f'Bottles:', end=' ')
    while bottles:
        print(bottles.pop(), end=' ')

print(f'\nWasted litters of water: {wasted_water}')