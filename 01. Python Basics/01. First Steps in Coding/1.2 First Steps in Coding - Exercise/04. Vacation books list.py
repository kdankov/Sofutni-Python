from math import floor;

pages_count = int(input())
pages_per_hour = int(input())
days = int(input())

time = pages_count / pages_per_hour / days

print(floor(time))
