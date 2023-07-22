numbers = input().split(' ')
text = input()

message = ''

for num in numbers:
    current_index = 0
    
    for i in num:
        current_index += int(i)
    
    current_index %= len(text)
    
    message += text[current_index]
    text = text.replace(text[current_index], '', 1)

print(message)