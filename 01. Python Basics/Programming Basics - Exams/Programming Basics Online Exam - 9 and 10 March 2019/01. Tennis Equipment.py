from math import floor, ceil

racket_price = float(input())
rackets_count = int(input())
shoes_pairs_count = int(input())

total_rackets_price = rackets_count * racket_price
shoes_price_per_pair = racket_price / 6
total_shoes_price = shoes_pairs_count * shoes_price_per_pair
other_equipment_price = (total_rackets_price + total_shoes_price) * 0.2

total_price = total_rackets_price + total_shoes_price + other_equipment_price

print(f'Price to be paid by Djokovic {floor(total_price / 8)}')
print(f'Price to be paid by sponsors {ceil(total_price * (7 / 8))}')