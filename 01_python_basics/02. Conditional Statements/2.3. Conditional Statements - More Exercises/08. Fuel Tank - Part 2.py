fuel_type = input()
litres = float(input())
has_club_card = input()

price = litres

if fuel_type == 'Gasoline':
    price *= 2.22 - 0.18 if has_club_card == 'Yes' else 2.22
elif fuel_type == 'Diesel':
    price *= 2.33 - 0.12 if has_club_card == 'Yes' else 2.33
elif fuel_type == 'Gas':
    price *= 0.93 - 0.08 if has_club_card == 'Yes' else 0.93
    
if litres > 25:
    price *= 0.9
elif litres >= 20:
    price *= 0.92
    
print(f'{price:.2f} lv.')