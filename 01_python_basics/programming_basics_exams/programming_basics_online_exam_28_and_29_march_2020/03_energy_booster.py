fruit = input()
set_size = input()
sets_purchased = int(input())

price = 0

if fruit == 'Watermelon':
    if set_size == 'small':
        price = 2 * 56
    elif set_size == 'big':
        price = 5 * 28.70
elif fruit == 'Mango':
    if set_size == 'small':
        price = 2 * 36.66
    elif set_size == 'big':
        price = 5 * 19.60
elif fruit == 'Pineapple':
    if set_size == 'small':
        price = 2 * 42.10
    elif set_size == 'big':
        price = 5 * 24.80
elif fruit == 'Raspberry':
    if set_size == 'small':
        price = 2 * 20
    elif set_size == 'big':
        price = 5 * 15.20
    
price *= sets_purchased

if price > 1000:
    price /= 2
elif price >= 400:
    price *= 0.85
    
print(f'{price:.2f} lv.')