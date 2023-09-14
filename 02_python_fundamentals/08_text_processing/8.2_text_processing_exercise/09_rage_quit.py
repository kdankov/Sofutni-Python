text = input().upper()

final_text = ''

current_text = ''
number = 0

unique_symbols = []

for i in range(len(text)):
    if not text[i].isdigit():
        current_text += text[i]
        
        if text[i] not in unique_symbols:
            unique_symbols.append(text[i])
    else:
        if i != len(text) - 1:
            if text[i + 1].isnumeric():
                number = int(text[i] + text[i + 1])
            else:
                number = int(text[i])
        else:
            number += int(text[i])
        
        current_text *= number
        final_text += current_text
        current_text = ''
        number = 0
    
print(f'Unique symbols used: {len(unique_symbols)}')
print(final_text)