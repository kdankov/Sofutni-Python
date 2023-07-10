budget = float(input())
extras = int(input())
clothes_price = float(input())

decor = budget * 0.1

if extras > 150:
    clothes_price *= 0.9
    
final_sum = extras * clothes_price + decor

if final_sum <= budget:
    print('Action!')
    print(f'Wingard starts filming with {budget - final_sum:.2f} leva left.')
else:
    print('Not enough money!')
    print(f'Wingard needs {final_sum - budget:.2f} leva more.')
