def forecast(*args):
    locations_dict = {}
    for location, weather in args:
        locations_dict[location] = weather

    sorted_locations = {k: v for k,v in sorted(locations_dict.items(), key=lambda x: (x[1], x[0]))}
    sunny = ''
    cloudy = ''
    rainy = ''

    for key, value in sorted_locations.items():
        if value == 'Sunny':
            sunny += f'{key} - {value}\n'
        elif value == 'Cloudy':
            cloudy += f'{key} - {value}\n'
        elif value == 'Rainy':
            rainy += f'{key} - {value}\n'

    return sunny + cloudy + rainy

print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))

print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))

print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))
