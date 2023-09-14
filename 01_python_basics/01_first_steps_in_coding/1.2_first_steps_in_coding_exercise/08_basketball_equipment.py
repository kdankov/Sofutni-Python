tax = int(input())

shoes_price = tax * 0.60
clothes_price = shoes_price * 0.8
ball_price = clothes_price / 4
accessories_price = ball_price / 5

price = tax + shoes_price + clothes_price + ball_price + accessories_price

print(f'{price:.2f}')