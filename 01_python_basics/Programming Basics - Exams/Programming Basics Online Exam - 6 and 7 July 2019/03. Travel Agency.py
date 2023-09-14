city = input()
package = input()
has_discount = input()
days = int(input())

price = 0

if days > 7:
    days -= 1

is_valid = True

if city == 'Bansko' or city == 'Borovets':
    if package == 'withEquipment':
        price = 100 * days if has_discount == 'no' else 100 * 0.9 * days
    elif package == 'noEquipment':
        price = 80 * days if has_discount == 'no' else 80 * 0.95 * days
    else:
        print('Invalid input!')
        is_valid = False
elif city == 'Varna' or city == 'Burgas':
    if package == 'withBreakfast':
        price = 130 * days if has_discount == 'no' else 130 * 0.88 * days
    elif package == 'noBreakfast':
        price = 100 * days if has_discount == 'no' else 100 * 0.93 * days
    else:
        print('Invalid input!')
        is_valid = False
else:
    print('Invalid input!')
    is_valid = False
    
if days <= 0:
    print('Days must be positive number!')
    is_valid = False

if is_valid:  
    print(f'The price is {price:.2f}lv! Have a nice time!')
