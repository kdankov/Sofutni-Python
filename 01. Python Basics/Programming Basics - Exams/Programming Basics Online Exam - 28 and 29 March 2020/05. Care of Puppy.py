bought_food = int(input())

bought_food *= 1000
needed_food = 0

current_food = input()

while current_food != 'Adopted':
    current_food = int(current_food)
    
    needed_food += current_food

    current_food = input()

if needed_food <= bought_food:
    print(f'Food is enough! Leftovers: {bought_food - needed_food} grams.')
else:
    print(f'Food is not enough. You need {needed_food - bought_food} grams more.')

