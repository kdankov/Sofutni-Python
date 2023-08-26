countries = input().split(', ')
capitals = input().split(', ')

zipped = dict(zip(countries, capitals))

[print(f'{country} -> {capital}') for country, capital in zipped.items()]
