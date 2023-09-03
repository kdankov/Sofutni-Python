import re

pattern = r'(\=|\/)([A-Z][a-zA-Z]{2,})\1'

travel_points = 0

text = input()

matches = re.finditer(pattern, text)

desitnations = []

for match in matches:
    desitnations.append(match.group(2))
    travel_points += len(match.group(2))
    
print(f'Destinations: {", ".join(desitnations)}')
print(f'Travel Points: {travel_points}')