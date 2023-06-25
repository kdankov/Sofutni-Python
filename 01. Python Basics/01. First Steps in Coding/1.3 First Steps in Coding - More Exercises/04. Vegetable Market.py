vegetables_price = float(input())
fruits_price = float(input())
vegetables_kg = int(input())
fruits_kg = int(input())

price = (vegetables_price * vegetables_kg + fruits_price * fruits_kg) / 1.94

print(f'{price:.2f}')