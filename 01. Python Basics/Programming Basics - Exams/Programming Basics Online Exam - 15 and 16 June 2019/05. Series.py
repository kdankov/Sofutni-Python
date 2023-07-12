budget = float(input())
series_count = int(input())

total_sum = 0

for i in range(series_count):
    current_series = input()
    price = float(input())
    
    if current_series == 'Thrones':
        price *= 0.5
    elif current_series == 'Lucifer':
        price *= 0.6
    elif current_series == 'Protector':
        price *= 0.7
    elif current_series == 'TotalDrama':
        price *= 0.8
    elif current_series == 'Area':
        price *= 0.9
        
    total_sum += price
    
if total_sum <= budget:
    print(f'You bought all the series and left with {budget - total_sum:.2f} lv.')
else:
    print(f'You need {total_sum - budget:.2f} lv. more to buy the series!')