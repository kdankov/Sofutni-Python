from math import floor

days_off = int(input())

total_play_time = (365 - days_off) * 63 + days_off * 127

hours = floor(abs(30000 - total_play_time) / 60)
minutes = abs(30000 - total_play_time) % 60

if total_play_time <= 30000:
    print('Tom sleeps well')
    print(f'{hours} hours and {minutes} minutes less for play')
else:
    print('Tom will run away')
    print(f'{hours} hours and {minutes} minutes more for play')