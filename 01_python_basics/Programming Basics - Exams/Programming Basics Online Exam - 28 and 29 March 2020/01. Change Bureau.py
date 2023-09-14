bitcoins_count = int(input())
chinese_yuans_count = float(input())
comission = float(input())

bitcoin = 1168 # leva
chinese_yuan = 0.15 # dollars
dollar = 1.76; # leva
euro = 1.95; # leva
    
sum = bitcoin * bitcoins_count + ((chinese_yuan * chinese_yuans_count) * dollar)
    
sum /= euro
sum -= sum * comission / 100

print(f'{sum:.2f}')
