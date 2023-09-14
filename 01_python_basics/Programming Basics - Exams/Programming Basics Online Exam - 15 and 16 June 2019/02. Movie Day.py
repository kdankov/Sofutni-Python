filming_time = int(input())
scenes_count = int(input())
scene_duration = int(input())

needed_time = scenes_count * scene_duration + filming_time * 0.15

if needed_time <= filming_time:
    print(f'You managed to finish the movie on time! You have {round(filming_time - needed_time)} minutes left!')
else:
    print(f'Time is up! To complete the movie you need {round(needed_time - filming_time)} minutes.')
