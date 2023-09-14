from math import floor

series_name = input()
seasons_count = int(input())
episodes_count = int(input())
episode_duration = float(input())

ads_duration_per_episode = episode_duration * 0.2
episode_duration += ads_duration_per_episode
speical_episodes_extra_duration = seasons_count * 10

total_watch_time = episode_duration * episodes_count * seasons_count + speical_episodes_extra_duration

print(f'Total time needed to watch the {series_name} series is {floor(total_watch_time)} minutes.')