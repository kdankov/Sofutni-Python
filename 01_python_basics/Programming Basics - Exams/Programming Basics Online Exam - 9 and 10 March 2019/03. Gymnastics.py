country = input()
equipment = input()

points = 0

if country == 'Russia':
    if equipment == 'ribbon':
        points = 9.100 + 9.400
    elif equipment == 'hoop':
        points = 9.300 + 9.800
    elif equipment == 'rope':
        points = 9.600 + 9.000
elif country == 'Bulgaria':
    if equipment == 'ribbon':
        points = 9.600 + 9.400
    elif equipment == 'hoop':
        points = 9.550 + 9.750
    elif equipment == 'rope':
        points = 9.500 + 9.400
elif country == 'Italy':
    if equipment == 'ribbon':
        points = 9.200 + 9.500
    elif equipment == 'hoop':
        points = 9.450 + 9.350
    elif equipment == 'rope':
        points = 9.700 + 9.150

points_to_reach_max = ((20 - points) / 20) * 100

print(f'The team of {country} get {points:.3f} on {equipment}.')
print(f'{points_to_reach_max:.2f}%')
