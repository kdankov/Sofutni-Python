import re

pattern = r'\b_([0-9A-Za-z]+)\b'

text = input()

matches = re.findall(pattern, text)

print(','.join(matches))
