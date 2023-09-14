food_quantity = float(input()) * 1000
hay_quantity = float(input()) * 1000
cover_quantity = float(input()) * 1000
weight = float(input()) * 1000

not_enough = False

for i in range(1, 31):
    food_quantity -= 300
    
    if i % 2 == 0:
        hay_quantity -= food_quantity * 0.05
    
    if i % 3 == 0:
        cover_quantity -= weight / 3
    
    if food_quantity <= 0 or hay_quantity <= 0 or cover_quantity <= 0:
        not_enough = True
    
if not_enough:
    print('Merry must go to the pet store!')
else:
    print(f'Everything is fine! Puppy is happy! Food: {food_quantity / 1000:.2f}, Hay: {hay_quantity / 1000:.2f}, Cover: {cover_quantity / 1000:.2f}.')
    