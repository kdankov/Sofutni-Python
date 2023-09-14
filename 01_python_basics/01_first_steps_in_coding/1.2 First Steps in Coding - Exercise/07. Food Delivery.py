chicken_menus = int(input())
fish_menus = int(input())
vegetarian_menus = int(input())

price = chicken_menus * 10.35 + fish_menus * 12.40 + vegetarian_menus * 8.15
price += price * 0.2 + 2.5

print(f'{price:.2f}')