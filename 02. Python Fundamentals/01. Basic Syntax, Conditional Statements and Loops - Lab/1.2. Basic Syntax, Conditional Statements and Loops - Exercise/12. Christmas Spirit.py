decorations_quantity = int(input())
days = int(input())

price = 0
spirit = 0

ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15

for i in range(1, days + 1):
    if i % 11 == 0:
        decorations_quantity += 2
    
    if i % 2 == 0:
        price += ornament_set_price * decorations_quantity
        spirit += 5
        
    if i % 3 == 0:
        price += (tree_skirt_price + tree_garland_price) * decorations_quantity
        spirit += 13
        
    if i % 5 == 0:
        price += tree_lights_price * decorations_quantity
        spirit += 17
        
    if i % 15 == 0:
        spirit += 30
        
    if i % 10 == 0:
        spirit -= 20
        price += tree_skirt_price + tree_garland_price + tree_lights_price
        
    if i % 10 == 0 and i == days:
        spirit -= 30
        
print(f'Total cost: {price}')
print(f'Total spirit: {spirit}')
