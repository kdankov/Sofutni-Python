import re

pattern = r'(#|\|)([A-Za-z\s]+)\1(\d{2,2}/\d{2,2}/\d{2,2})\1(\d{1,5})\1'

text = input()

matches = re.findall(pattern, text)

new_list = []
calories_sum = 0

for match in re.finditer(pattern, text):
    new_list.append([match.group(2), match.group(3), match.group(4)])
    calories_sum += int(match.group(4))
    
days = calories_sum // 2000

print(f"You have food to last you for: {days} days!")

for match in new_list:
    print(f"Item: {match[0]}, Best before: {match[1]}, Nutrition: {match[2]}")