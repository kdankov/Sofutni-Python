amount = round(float(input()) * 100) 

coins = 0

while amount > 0:
    if amount >= 200:
        amount -= 200
    elif amount >= 100:
        amount -= 100
    elif amount >= 50:
        amount -= 50
    elif amount >= 20:
        amount -= 20
    elif amount >= 10:
        amount -= 10
    elif amount >= 5:
        amount -= 5
    elif amount >= 2:
        amount -= 2
    else:
        amount -= 1
    
    coins += 1
    
print(coins)