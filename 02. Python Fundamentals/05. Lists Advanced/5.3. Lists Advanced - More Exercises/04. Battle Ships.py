rows = int(input())
battle_ships = []
count = 0

for row in range(rows):
    battle_ship = [int(num) for num in input().split()]
    battle_ships.append(battle_ship)

attack = input().split()

while attack:
    attack_sq = attack[0].split("-")
    row = int(attack_sq[0])
    col = int(attack_sq[1])
    for element in range(len(battle_ships)):
        if element == row:
            columns = battle_ships[element]
            if columns[col] != 0:
                columns[col] -= 1
                if columns[col] == 0:
                    count += 1
    attack.pop(0)

print(count)