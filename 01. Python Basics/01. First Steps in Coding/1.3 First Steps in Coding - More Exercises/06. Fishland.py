mackerel_price_per_kg = float(input())
sprat_price_per_kg = float(input())
bonitoKg = float(input())
scadKg = float(input())
clamsKg = int(input())

bonito_price = bonitoKg * (mackerel_price_per_kg * 1.6)
scad_price = scadKg * (sprat_price_per_kg * 1.8)
clamsPrice = clamsKg * 7.50

final_price = bonito_price + scad_price + clamsPrice

print(f'{final_price:.2f}')