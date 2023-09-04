n = int(input())

heroes_dict = {}

MAX_HP = 100
MAX_MP = 200

for i in range(n):
    add_hero = input().split()
    name = add_hero[0]
    initial_hp = int(add_hero[1])
    initial_mp = int(add_hero[2])
    
    heroes_dict[name] = {'HP': initial_hp, 'MP': initial_mp}

current_line = input()

while current_line != 'End':
    tokens = current_line.split(' - ')
    command = tokens[0]
    hero_name = tokens[1]
    
    if command == 'CastSpell':
        needed_mp = int(tokens[2])
        spell_name = tokens[3]
        
        if heroes_dict[hero_name]['MP'] >= needed_mp:
            heroes_dict[hero_name]['MP'] -= needed_mp
            print(f'{hero_name} has successfully cast {spell_name} and now has {heroes_dict[hero_name]["MP"]} MP!')
        else:
            print(f'{hero_name} does not have enough MP to cast {spell_name}!')
    
    elif command == 'TakeDamage':
        damage = int(tokens[2])
        attacker = tokens[3]
        
        heroes_dict[hero_name]['HP'] -= damage
        
        if heroes_dict[hero_name]['HP'] > 0:
            print(f'{hero_name} was hit for {damage} HP by {attacker} and now has {heroes_dict[hero_name]["HP"]} HP left!')
        else:
            del heroes_dict[hero_name]
            print(f'{hero_name} has been killed by {attacker}!')
    
    elif command == 'Recharge':
        amount = int(tokens[2])
        
        if heroes_dict[hero_name]['MP'] + amount >= MAX_MP:
            amount = MAX_MP - heroes_dict[hero_name]['MP']
            heroes_dict[hero_name]['MP'] = MAX_MP
        else:
            heroes_dict[hero_name]['MP'] += amount
        
        print(f'{hero_name} recharged for {amount} MP!')
        
    elif command == 'Heal':
        amount = int(tokens[2])
        
        if heroes_dict[hero_name]['HP'] + amount >= MAX_HP:
            amount = MAX_HP - heroes_dict[hero_name]['HP']
            heroes_dict[hero_name]['HP'] = MAX_HP
        else:
            heroes_dict[hero_name]['HP'] += amount
            
        print(f'{hero_name} healed for {amount} HP!')
        
    current_line = input()
    
for key, value in heroes_dict.items():
    print(key)
    print(f'  HP: {value["HP"]}')
    print(f'  MP: {value["MP"]}')