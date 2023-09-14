budget = float(input())
flour_price_per_kg = float(input())

eggs_price_per_pack = flour_price_per_kg * 0.75
milk_price = (flour_price_per_kg * 1.25) / 4

easter_bread_price = flour_price_per_kg + eggs_price_per_pack + milk_price

colored_eggs = 0
loaves_of_bread = 0

while budget > easter_bread_price:
    budget -= easter_bread_price
    loaves_of_bread += 1
    colored_eggs += 3
    
    if loaves_of_bread % 3 == 0:
        colored_eggs = colored_eggs - (loaves_of_bread - 2)
    
print(f'You made {loaves_of_bread} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')
