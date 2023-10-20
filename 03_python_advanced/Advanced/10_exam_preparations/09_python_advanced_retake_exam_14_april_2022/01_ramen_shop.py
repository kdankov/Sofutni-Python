from collections import deque

ramen_bowls = [int(x) for x in input().split(', ')]
customers = deque([int(x) for x in input().split(', ')])

while ramen_bowls and customers:
    current_ramen_bowl = ramen_bowls[-1]
    current_customer = customers[0]

    if current_ramen_bowl == current_customer:
        ramen_bowls.pop()
        customers.popleft()
        continue
    elif current_ramen_bowl > current_customer:
        ramen_bowls[-1] -= current_customer
        customers.popleft()
        continue
    else:
        customers[0] -= current_ramen_bowl
        ramen_bowls.pop()

if not customers:
    print('Great job! You served all the customers.')
    if ramen_bowls:
        print(f'Bowls of ramen left: {", ".join([str(x) for x in ramen_bowls])}')
else:
    print('Out of ramen! You didn\'t manage to serve all customers.')
    if customers:
        print(f'Customers left: {", ".join([str(x) for x in customers])}')
