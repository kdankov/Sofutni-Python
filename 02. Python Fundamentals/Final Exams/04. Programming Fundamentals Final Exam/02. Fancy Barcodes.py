import re

pattern = r'\@\#+[A-Z][a-zA-Z0-9]{4,}[A-Z]\@\#+'

n = int(input())

for i in range(n):
    text = input()
    
    product_group = ''
    
    match = re.fullmatch(pattern, text)
    
    if match is None:
        print('Invalid barcode')
        continue
    
    valid = match[0]
    
    for ch in valid:
        if ch.isdigit():
            product_group += ch
                
    if len(product_group) == 0:
        product_group = '00'
        
    print(f'Product group: {product_group}')
