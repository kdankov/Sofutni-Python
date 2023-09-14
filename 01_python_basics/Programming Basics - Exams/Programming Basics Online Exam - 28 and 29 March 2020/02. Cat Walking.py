minutes_walking_per_day = int(input())
walks_per_day = int(input())
calories_intake_per_day = int(input())

calories_burned = 5 * (minutes_walking_per_day * walks_per_day)

if calories_intake_per_day / 2 <= calories_burned:
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {calories_burned}.')
else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {calories_burned}.')
