juniors = int(input())
seniors = int(input())
trace_type = input()

collected_money = 0

if trace_type == 'trail':
    collected_money = juniors * 5.50 + seniors * 7
elif trace_type == 'cross-country':
    collected_money = juniors * 8 + seniors * 9.50
    
    if juniors + seniors >= 50:
        collected_money *= 0.75
elif trace_type == 'downhill':
    collected_money = juniors * 12.25 + seniors * 13.75
elif trace_type == 'road':
    collected_money = juniors * 20 + seniors * 21.50

collected_money *= 0.95

print(f'{collected_money:.2f}')