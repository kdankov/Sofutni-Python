flour_price_per_kg = float(input())
flour_kg = float(input())
sugar_kg = float(input())
eggs = int(input())
yeast = int(input())

sugar_price = flour_price_per_kg * 0.75
eggs_price = flour_price_per_kg * 1.1
yeast_price = sugar_price * 0.2

total_sum = flour_price_per_kg * flour_kg + sugar_price * sugar_kg + eggs_price * eggs + yeast_price * yeast

print(f'{total_sum:.2f}')