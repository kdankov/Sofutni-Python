rent = float(input())

cake_price = rent * 0.2
drinks = cake_price * 0.55
animator = rent / 3

total_price = rent + cake_price + drinks + animator

print(f'{total_price:.1f}')
