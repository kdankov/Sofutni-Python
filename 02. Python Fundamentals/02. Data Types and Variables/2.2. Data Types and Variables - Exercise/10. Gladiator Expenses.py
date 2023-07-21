lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

aureus = 0

shield_broken_times = 0

for i in range(1, lost_fights_count + 1):
    if i % 2 == 0:
        aureus += helmet_price
    
    if i % 3 == 0:
        aureus += sword_price
        
    if i % 2 == 0 and i % 3 == 0:
        aureus += shield_price
        shield_broken_times += 1
    
    if shield_broken_times == 2:
        aureus += armor_price
        shield_broken_times = 0
        
print(f'Gladiator expenses: {aureus:.2f} aureus')
