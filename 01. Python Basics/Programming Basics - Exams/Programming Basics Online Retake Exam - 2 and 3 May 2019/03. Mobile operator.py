contract_term = input()
contract_type = input()
mobile_data = input()
months = int(input())

price = 0

if contract_term == 'one':
    if contract_type == 'Small':
        price = 9.98 * months if mobile_data == 'no' else 15.48 * months
    elif contract_type == 'Middle':
        price = 18.99 * months if mobile_data == 'no' else 23.34 * months
    elif contract_type == 'Large':
        price = 25.98 * months if mobile_data == 'no' else 30.33 * months
    elif contract_type == 'ExtraLarge':
        price = 35.99 * months if mobile_data == 'no' else 39.84 * months
elif contract_term == 'two':
    if contract_type == 'Small':
        price = 8.58 * months if mobile_data == 'no' else 14.08 * months
    elif contract_type == 'Middle':
        price = 17.09 * months if mobile_data == 'no' else 21.44 * months
    elif contract_type == 'Large':
        price = 23.59 * months if mobile_data == 'no' else 27.94 * months
    elif contract_type == 'ExtraLarge':
        price = 31.79 * months if mobile_data == 'no' else 35.64 * months
    
    price *= 0.9625
    
print(f'{price:.2f} lv.')