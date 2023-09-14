from math import floor, ceil

magnolias_count = int(input())
hyacinths_count = int(input())
roses_count = int(input())
cactuses_count = int(input())
gift_price = float(input())

collected_sum = (magnolias_count * 3.25 + hyacinths_count * 4 + roses_count * 3.50 + cactuses_count * 8) * 0.95

if collected_sum >= gift_price:
    print(f'She is left with {floor(collected_sum - gift_price)} leva.')
else:
    print(f'She will have to borrow {ceil(gift_price - collected_sum)} leva.')
