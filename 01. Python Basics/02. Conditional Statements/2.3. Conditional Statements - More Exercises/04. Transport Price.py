kilometres = int(input())
day_time = input()

price = 0

if kilometres < 20:
    if day_time == 'day':
        price = 0.70 + 0.79 * kilometres
    elif day_time == 'night':
        price = 0.70 + 0.90 * kilometres
elif kilometres < 100:
        price = 0.09 * kilometres
else:
    price = 0.06 * kilometres

print(f'{price:.2f}')