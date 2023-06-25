metres = float(input())

price = metres * 7.61
discount = price * 0.18

print(f'The final price is: {price - discount:.2f} lv.')
print(f'The discount is: {discount:.2f} lv.')