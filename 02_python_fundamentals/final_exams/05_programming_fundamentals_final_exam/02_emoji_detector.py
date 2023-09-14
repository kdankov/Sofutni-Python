import re

pattern = r'(\:\:|\*\*)([A-Z][a-z]{2,})\1'

cool_threshold = 1

all_emojis = []
cool_emojis = []

text = input()

for ch in text:
    if ch.isdigit():
        cool_threshold *= int(ch)
        
matches = re.finditer(pattern, text)

for match in matches:
    all_emojis.append(match.group(0))
    
    current_coolness = 0
    current_emoji = match.group(2)
    
    for ch in current_emoji:
        current_coolness += ord(ch)
        
    if current_coolness >= cool_threshold:
        cool_emojis.append(match.group(0))

print(f'Cool threshold: {cool_threshold}')

print(f'{len(all_emojis)} emojis found in the text. The cool ones are:')

print('\n'.join(cool_emojis))