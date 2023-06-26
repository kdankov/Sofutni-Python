budget = float(input())
gpu_count = int(input())
cpu_count = int(input())
ram_count = int(input())

gpu_price = gpu_count * 250
cpu_price = cpu_count * (gpu_price * 0.35)
ram_price = ram_count * (gpu_price * 0.1)

total = gpu_price + cpu_price + ram_price

if gpu_count > cpu_count:
    total *= 0.85
    
if total <= budget:
    print(f'You have {budget - total:.2f} leva left!')
else:
    print(f'Not enough money! You need {total - budget:.2f} leva more!')
