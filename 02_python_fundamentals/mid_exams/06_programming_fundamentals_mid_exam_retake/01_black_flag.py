days = int(input())
daily_plunder = int(input())
target_plunder = float(input())

collected_plunder = 0

for i in range(1, days + 1):
    collected_plunder += daily_plunder
    
    if i % 3 == 0:
        collected_plunder += daily_plunder / 2
        
    if i % 5 == 0:
        collected_plunder *= 0.7
        
if collected_plunder >= target_plunder:
    print(f'Ahoy! {collected_plunder:.2f} plunder gained.')
else:
    print(f'Collected only {collected_plunder * 100 / target_plunder:.2f}% of the plunder.')
    