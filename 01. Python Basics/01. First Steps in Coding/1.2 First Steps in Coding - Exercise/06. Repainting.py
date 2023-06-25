nylon = int(input())
paint = int(input())
diluent = int(input())
hours = int(input())

price = (nylon + 2) * 1.50 + (paint * 1.1) * 14.50 + diluent * 5 + 0.40

price += (price * 0.3) * hours

print(price)