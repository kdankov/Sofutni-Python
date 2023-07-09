from math import ceil

people_count = int(input())
entry_tax = float(input())
lounger_price = float(input())
umbrella_price = float(input())

total_entry_tax = people_count * entry_tax
total_loungers_price = ceil(people_count * 0.75) * lounger_price
total_umbrellas_price = ceil(people_count / 2) * umbrella_price

total_sum = total_entry_tax + total_loungers_price + total_umbrellas_price

print(f'{total_sum:.2f} lv.')