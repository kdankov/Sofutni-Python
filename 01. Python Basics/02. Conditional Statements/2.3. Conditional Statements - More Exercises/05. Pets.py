from math import ceil, floor

days = int(input())
food_left = int(input())
dog_food_per_day = float(input())
cat_food_per_day = float(input())
turtle_food_per_day = float(input())

food_needed = days * dog_food_per_day + days * \
    cat_food_per_day + days * (turtle_food_per_day / 1000)

if food_needed <= food_left:
    print(f'{floor(food_left - food_needed)} kilos of food left.')
else:
    print(f'{ceil(food_needed - food_left)} more kilos of food are needed.')