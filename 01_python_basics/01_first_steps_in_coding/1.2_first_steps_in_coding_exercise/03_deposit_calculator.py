deposited_sum = float(input())
period = int(input())
percentage = float(input())

sum = deposited_sum + period * ((deposited_sum * (percentage / 100)) / 12)

print(f'{sum:.2f}')