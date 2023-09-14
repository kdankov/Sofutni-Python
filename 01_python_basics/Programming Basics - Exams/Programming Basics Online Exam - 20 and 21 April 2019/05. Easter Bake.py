from math import ceil

easter_breads_count = int(input())

total_sugar_packages = 0
total_flour_packages = 0

max_used_products = {
    'sugar': 0,
    'flour': 0
}

for i in range(easter_breads_count):
    used_sugar = int(input())
    used_flour = int(input())
    
    total_sugar_packages += used_sugar
    total_flour_packages += used_flour
    
    if used_sugar > max_used_products['sugar']:
        max_used_products['sugar'] = used_sugar
    
    if used_flour > max_used_products['flour']:
        max_used_products['flour'] = used_flour
        
total_sugar_packages = ceil(total_sugar_packages / 950)
total_flour_packages = ceil(total_flour_packages / 750)

print(f'Sugar: {total_sugar_packages}')
print(f'Flour: {total_flour_packages}')
print(f'Max used flour is {max_used_products["flour"]} grams, max used sugar is {max_used_products["sugar"]} grams.')
