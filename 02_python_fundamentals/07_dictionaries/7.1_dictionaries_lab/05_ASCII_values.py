characters = input().split(', ')

chars_dict = {}

for char in characters:
    if char not in chars_dict:
        chars_dict[char] = ord(char)

print(chars_dict)
