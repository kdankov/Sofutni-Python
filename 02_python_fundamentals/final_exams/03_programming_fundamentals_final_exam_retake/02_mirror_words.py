import re

command = input()

list_matches = []

mirror_matches = []

pattern = r"(\@|\#)([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1"

matches = re.finditer(pattern,command)

for match in matches:
    list_matches.append(match.group(2))
    list_matches.append(match.group(3))
    
if len(list_matches) != 0:
    print(f"{int((len(list_matches)) / 2)} word pairs found!")
else:
    print(f"No word pairs found!")
    
for i in range (1,len(list_matches),2):
    if (list_matches[i][::-1]) == (list_matches[i-1]):
        mirror_matches.append(list_matches[i-1]+" <=> " + list_matches[i])
        
if len(mirror_matches) > 0:
    print("The mirror words are:")
    print(', '.join(mirror_matches))
else:
    print("No mirror words!")