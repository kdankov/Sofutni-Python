luggage_price_over_20_kg = float(input())
luggage_kg = float(input())
days_until_trip = int(input())
luggages_count = int(input())

price = 0

if luggage_kg < 10:
    price = luggage_price_over_20_kg * 0.2
elif luggage_kg <= 20:
    price = luggage_price_over_20_kg / 2
else:
    price = luggage_price_over_20_kg
    
if days_until_trip > 30:
    price *= 1.1
elif 7 <= days_until_trip <= 30:
    price *= 1.15
else:
    price *= 1.4

price *= luggages_count
    
print(f'The total price of bags is: {price:.2f} lv.')