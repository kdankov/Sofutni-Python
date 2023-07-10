rent = int(input())

statuettes_price = rent * 0.7
catering_price = statuettes_price * 0.85
voicing = catering_price / 2

total_expenses = rent + statuettes_price + catering_price + voicing

print(f'{total_expenses:.2f}')