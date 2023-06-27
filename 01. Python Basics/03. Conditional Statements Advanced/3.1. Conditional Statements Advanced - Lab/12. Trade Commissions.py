city = input()
sales = float(input())

invalid = False
comission = sales

if city == 'Sofia':
    if 0 <= sales <= 500:
        comission *= 0.05
    elif 500 < sales <= 1000:
        comission *= 0.07
    elif 1000 < sales <= 10000:
        comission *= 0.08
    elif sales > 10000:
        comission *= 0.12
    else:
        invalid = True
elif city == 'Varna':
    if 0 <= sales <= 500:
        comission *= 0.045
    elif 500 < sales <= 1000:
        comission *= 0.075
    elif 1000 < sales <= 10000:
        comission *= 0.1
    elif sales > 10000:
        comission *= 0.13
    else:
        invalid = True
elif city == 'Plovdiv':
    if 0 <= sales <= 500:
        comission *= 0.055
    elif 500 < sales <= 1000:
        comission *= 0.08
    elif 1000 < sales <= 10000:
        comission *= 0.12
    elif sales > 10000:
        comission *= 0.145
    else:
        invalid = True
else:
    invalid = True
    
if invalid:
    print('error')
else:
    print(f'{comission:.2f}')