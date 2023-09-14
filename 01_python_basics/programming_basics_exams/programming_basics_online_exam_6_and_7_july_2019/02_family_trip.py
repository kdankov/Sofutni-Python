budget = float(input())
nights_count = int(input())
price_per_night = float(input())
extra_expenses_percentage = int(input())

if nights_count > 7:
    price_per_night *= 0.95

all_nights_price = price_per_night * nights_count
extra_expenses = (budget * extra_expenses_percentage) / 100

total_sum = all_nights_price + extra_expenses

if total_sum <= budget:
    print(f'Ivanovi will be left with {budget - total_sum:.2f} leva after vacation.')
else:
    print(f'{total_sum - budget:.2f} leva needed.')