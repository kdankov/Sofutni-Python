from collections import deque

substrings = deque(input().split())

main_colors = ['red', 'yellow', 'blue']

secondary_colors = {
    "orange": {"yellow", "red"},
    "purple": {"red", "blue"},
    "green": {"yellow", "blue"},
}

colors_found = []

while substrings:
    first_substring = substrings.popleft()
    last_substring = substrings.pop() if substrings else ''

    for color in (first_substring + last_substring, last_substring + first_substring):
        if color in main_colors or color in secondary_colors:
            colors_found.append(color)
            break
    else:
        for ch in (first_substring[:-1], last_substring[:-1]):
            if ch:
                substrings.insert(len(substrings) // 2, ch)

for color in set(secondary_colors.keys()).intersection(colors_found):
    if not secondary_colors[color].issubset(colors_found):
        colors_found.remove(color)

print(colors_found)