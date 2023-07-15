eggs_size = input()
eggs_color = input()
count = int(input())

price = 0

if eggs_size == 'Large':
    if eggs_color == 'Red':
        price = 16 * count
    elif eggs_color == 'Green':
        price = 12 * count
    elif eggs_color == 'Yellow':
        price = 9 * count
elif eggs_size == 'Medium':
    if eggs_color == 'Red':
        price = 13 * count
    elif eggs_color == 'Green':
        price = 9 * count
    elif eggs_color == 'Yellow':
        price = 7 * count
elif eggs_size == 'Small':
    if eggs_color == 'Red':
        price = 9 * count
    elif eggs_color == 'Green':
        price = 8 * count
    elif eggs_color == 'Yellow':
        price = 5 * count

price *= 0.65

print(f'{price:.2f} leva.')