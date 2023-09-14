from math import floor

current_record = float(input())
distance = float(input())
seconds_per_metre = float(input())

time = distance * seconds_per_metre

added_time = floor(distance / 15) * 12.5

time += added_time

if time < current_record:
    print(f'Yes, he succeeded! The new world record is {time:.2f} seconds.')
else:
    print(f'No, he failed! He was {abs(current_record - time):.2f} seconds slower.')

    