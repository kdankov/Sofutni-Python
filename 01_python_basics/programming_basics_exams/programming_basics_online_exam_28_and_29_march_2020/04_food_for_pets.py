days = int(input())
total_food = float(input())

biscuits= 0

total_food_eaten = 0
dog_food_eaten = 0
cat_food_eaten = 0

for i in range(1, days + 1):
    dog_food = int(input())
    cat_food = int(input())
    
    total_food_eaten += dog_food + cat_food
    
    dog_food_eaten += dog_food
    cat_food_eaten += cat_food
    
    if i % 3 == 0:
        biscuits += (dog_food + cat_food) * 0.1

dog_food_eaten = dog_food_eaten * 100 / total_food_eaten
cat_food_eaten = cat_food_eaten * 100 / total_food_eaten
total_food_eaten = total_food_eaten * 100 / total_food

print(f'Total eaten biscuits: {round(biscuits)}gr.')
print(f'{total_food_eaten:.2f}% of the food has been eaten.')
print(f'{dog_food_eaten:.2f}% eaten from the dog.')
print(f'{cat_food_eaten:.2f}% eaten from the cat.')
