from functools import reduce

line = input()

products = {}

while line != 'buy':
    current_product = line.split()
    product_name = current_product[0]
    price = float(current_product[1])
    quantity = int(current_product[2])
    
    if product_name not in products:
        products[product_name] = [0, 0]
    products[product_name][0] = price
    products[product_name][1] += quantity
    
    line = input()

[print(f'{key} -> {reduce((lambda x, y: x * y), value):.2f}') for key, value in products.items()]
