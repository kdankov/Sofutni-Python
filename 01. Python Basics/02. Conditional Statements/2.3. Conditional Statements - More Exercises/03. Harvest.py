from math import floor, ceil

vineyard_area = int(input())
grapes = float(input())
wine_needed = int(input())
workers = int(input())

total_wine = (40 * (vineyard_area * grapes) / 100) / 2.5

if total_wine >= wine_needed:
    print(f'Good harvest this year! Total wine: {floor(total_wine)} liters.')
    print(f'{ceil(total_wine - wine_needed)} liters left -> {ceil((total_wine - wine_needed) / workers)} liters per person.')
else:
    print(f'It will be a tough winter! More {floor(wine_needed - total_wine)} liters wine needed.')