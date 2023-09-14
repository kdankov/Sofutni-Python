def solve(product, quantity):
    price = None
    
    if product == 'coffee':
        price = quantity * 1.50
    elif product == 'water':
        price = quantity * 1
    elif product == 'coke':
        price = quantity * 1.4
    elif product == 'snacks':
        price = quantity * 2
        
    return f'{price:.2f}'

input_product = input()
input_quantity = int(input())

print(solve(input_product, input_quantity))