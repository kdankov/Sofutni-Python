import re

pattern = r'www\.[a-zA-Z0-9\-]+(\.[a-z]+)+'

while True:
    text = input()
    
    if not text:
        break
    
    matches = re.finditer(pattern, text) 
    
    for match in matches:
        print(match[0])