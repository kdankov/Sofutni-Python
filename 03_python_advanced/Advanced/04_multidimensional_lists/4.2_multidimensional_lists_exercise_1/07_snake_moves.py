from collections import deque

rows, cols = [int(x) for x in input().split()]
snake = list(input())

snake_queue = deque(snake)

for row in range(rows):
    while len(snake_queue) < cols:
        snake_queue.extend(snake)

    if row % 2 == 0:
        print(*[snake_queue.popleft() for _ in range(cols)], sep="")
    else:
        print(*[snake_queue.popleft() for _ in range(cols)][::-1], sep="")