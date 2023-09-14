guests_count = int(input())
couvert_price_per_guest = float(input())
budget = float(input())

if 10 <= guests_count <= 15:
    couvert_price_per_guest *= 0.85
elif 15 < guests_count <= 20:
    couvert_price_per_guest *= 0.8
elif 20 < guests_count:
    couvert_price_per_guest *= 0.75

price = guests_count * couvert_price_per_guest + budget * 0.1

if price <= budget:
    print(f'It is party time! {budget - price:.2f} leva left.')
else:
    print(f'No party! {price - budget:.2f} leva needed.')
