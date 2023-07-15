annual_fee = int(input())

shoes_price = annual_fee * 0.6
clothes_price = shoes_price * 0.8
ball_price = clothes_price / 4
accessories_price = ball_price / 5

total_price = annual_fee + shoes_price + clothes_price + ball_price + accessories_price

print(f'{total_price:.2f}')