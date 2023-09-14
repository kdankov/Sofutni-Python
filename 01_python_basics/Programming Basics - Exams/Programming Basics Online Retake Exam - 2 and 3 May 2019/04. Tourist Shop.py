budget = float(input())

price = 0
count = 0

current_product = input()

flag = False

while current_product != 'Stop':
    count += 1
    current_price = float(input())
    
    if count % 3 == 0:
        current_price /= 2

    budget -= current_price
    price += current_price
    
    if budget < 0:
        flag = True
        break
    
    current_product = input()

if not flag:
    print(f'You bought {count} products for {price:.2f} leva.')
else:
    print(f'You don\'t have enough money!')
    print(f'You need {abs(budget):.2f} leva!')