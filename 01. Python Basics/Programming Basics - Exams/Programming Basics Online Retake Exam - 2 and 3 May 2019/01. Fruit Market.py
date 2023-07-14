strawberries_price = float(input())
bananas_kg = float(input())
oranges_kg = float(input())
raspberries_kg = float(input())
strawberries_kg = float(input())

raspberries_price = strawberries_price / 2
oranges_price = raspberries_price * 0.6
bananas_price = raspberries_price * 0.2

final_price = strawberries_price * strawberries_kg + bananas_price * bananas_kg + oranges_price * oranges_kg + raspberries_price * raspberries_kg

print(f'{final_price:.2f}')