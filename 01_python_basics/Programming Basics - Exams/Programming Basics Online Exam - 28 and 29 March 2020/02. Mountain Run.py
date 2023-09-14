from math import floor

record_in_seconds = float(input())
distance_in_metres = float(input())
time_for_one_meter = float(input())

distance_in_seconds = distance_in_metres * time_for_one_meter

total_time = distance_in_seconds + floor(distance_in_metres / 50) * 30

if total_time < record_in_seconds:
    print(f'Yes! The new record is {total_time:.2f} seconds.')
else:
    print(f'No! He was {total_time - record_in_seconds:.2f} seconds slower.')
    
