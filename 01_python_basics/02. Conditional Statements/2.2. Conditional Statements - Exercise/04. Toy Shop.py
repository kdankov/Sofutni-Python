excursion_price = float(input())
puzzles = int(input())
dolls = int(input())
teddy_bears = int(input())
minions = int(input())
trucks = int(input())

money_collected = puzzles * 2.60 + dolls * 3 + teddy_bears * 4.10 + minions * 8.20 + trucks * 2
toys_count = puzzles + dolls + teddy_bears + minions + trucks

if toys_count >= 50:
    money_collected *= 0.75

money_collected *= 0.9

if money_collected >= excursion_price:
    print(f'Yes! {money_collected - excursion_price:.2f} lv left.')
else:
    print(f'Not enough money! {excursion_price - money_collected:.2f} lv needed.')