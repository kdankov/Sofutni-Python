import re

pattern = r'\%([A-Z][a-z]+)\%[^\|\$\%\.]*?\<(\w+)\>[^\|\$\%\.]*?\|([0-9]+)\|[^\|\$\%\.]*?([0-9.]+[0-9])\$'

current_line = input()

total_income = 0

while current_line != 'end of shift':
    match = re.fullmatch(pattern, current_line)
    
    if match is None:
        current_line = input()
        continue

    name = match[1]
    product = match[2]
    quantity = int(match[3])
    price = float(match[4])
    
    current_amount = price * quantity
    total_income += current_amount
    
    print(f"{name}: {product} - {current_amount:.2f}")
    
    current_line = input()
    
print(f'Total income: {total_income:.2f}')