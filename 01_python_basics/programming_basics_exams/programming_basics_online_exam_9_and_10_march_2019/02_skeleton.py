minutes = int(input())
seconds = int(input())
length = float(input())
seconds_for_100_metres = int(input())

total_time_in_seconds = minutes * 60 + seconds
slowing = (length / 120) * 2.5

marins_time = (length / 100) * seconds_for_100_metres - slowing

if marins_time <= total_time_in_seconds:
    print(f'Marin Bangiev won an Olympic quota!')
    print(f'His time is {marins_time:.3f}.')
else:
    print(f'No, Marin failed! He was {marins_time - total_time_in_seconds:.3f} second slower.')