from math import ceil

people_count = int(input())
capacity = int(input())

courses = ceil(people_count / capacity)

print(courses)