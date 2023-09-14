from collections import deque

food_quantity = int(input())

orders_queue = deque([int(x) for x in input().split()])

print(max(orders_queue))

not_enough_food = False

while orders_queue:
    if food_quantity >= orders_queue[0]:
        food_quantity -= orders_queue.popleft()
    else:
        not_enough_food = True
        print(f'Orders left: {" ".join([str(x) for x in orders_queue])}')
        break

if not not_enough_food:
    print(f'Orders complete')
