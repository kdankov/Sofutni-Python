from collections import deque

monsters_armors = deque([int(x) for x in input().split(',')])
striking_impact = [int(x) for x in input().split(',')]

killed_monsters_count = 0

while monsters_armors and striking_impact:
    current_monster_armor = monsters_armors.popleft()
    current_strike = striking_impact.pop()

    if current_strike >= current_monster_armor:
        killed_monsters_count += 1
        current_strike -= current_monster_armor
        if striking_impact:
            striking_impact[-1] += current_strike
        elif not striking_impact and current_strike > 0:
            striking_impact.append(current_strike)
    else:
        current_monster_armor -= current_strike
        monsters_armors.append(current_monster_armor)

if not monsters_armors:
    print('All monsters have been killed!')
if not striking_impact:
    print('The soldier has been defeated.')

print(f'Total monsters killed: {killed_monsters_count}')