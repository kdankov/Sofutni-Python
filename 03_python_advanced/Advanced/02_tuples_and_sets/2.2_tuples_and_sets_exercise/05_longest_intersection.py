n = int(input())

longest_intersection = set()

for _ in range(n):
    data = input().split('-')
    first_intersection_range = data[0].split(',')
    first_start = int(first_intersection_range[0])
    first_end = int(first_intersection_range[1])

    second_intersection_range = data[1].split(',')
    second_start = int(second_intersection_range[0])
    second_end = int(second_intersection_range[1])

    current_intersection = set(range(first_start, first_end + 1)) & set(range(second_start, second_end + 1))
    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection

sorted_intersection = sorted(longest_intersection)

print(f'Longest intersection is '
      f'[{", ".join([str(x) for x in sorted_intersection])}] with length {len(longest_intersection)}')