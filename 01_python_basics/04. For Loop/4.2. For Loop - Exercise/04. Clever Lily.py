age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

toys_count = 0
money = 0

current_money = 10

for i in range(1, age + 1):
    if i % 2 == 0:
        money += current_money - 1
        current_money += 10
    else:
        toys_count += 1

money += toys_count * toy_price

if money >= washing_machine_price:
    print(f'Yes! {money - washing_machine_price:.2f}')
else:
    print(f'No! {washing_machine_price - money:.2f}')