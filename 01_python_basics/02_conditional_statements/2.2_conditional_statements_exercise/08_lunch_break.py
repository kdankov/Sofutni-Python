from math import ceil

series_name = input()
episode_duration = int(input())
break_duration = int(input())

time_for_lunch = break_duration * (1 / 8)
time_for_rest = break_duration * (1 / 4)

time_left = break_duration - time_for_lunch - time_for_rest

if time_left >= episode_duration:
    print(f'You have enough time to watch {series_name} and left with {ceil(time_left - episode_duration)} minutes free time.')
else:
    print(f'You don\'t have enough time to watch {series_name}, you need {ceil(episode_duration - time_left)} more minutes.')