from math import floor
from collections import deque

expression = input().split()

numbers_queue = deque()

for el in expression:
    current_sum = 0

    if el.lstrip('-').isdigit():
        numbers_queue.append(int(el))
    else:
        current_sum = numbers_queue.popleft()

        if el == '*':
            while numbers_queue:
                current_sum *= numbers_queue.popleft()

        elif el == '+':
            while numbers_queue:
                current_sum += numbers_queue.popleft()

        elif el == '-':
            while numbers_queue:
                current_sum -= numbers_queue.popleft()

        elif el == '/':
            while numbers_queue:
                current_sum = floor(current_sum / numbers_queue.popleft())

        numbers_queue.append(current_sum)


print(numbers_queue.popleft())
