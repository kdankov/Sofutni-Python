pens_packages = int(input())
markers_packages = int(input())
detergent_litres = int(input())
discout_percent = int(input())

discout_percent /= 100

sum = (pens_packages * 5.80 + markers_packages * 7.20 +
       detergent_litres * 1.20) * (1 - discout_percent)

print(f'{sum:.2f}')
