stadium_capacity = int(input())
fans_count = int(input())

sector_a_fans = 0
sector_b_fans = 0
sector_v_fans = 0
sector_g_fans = 0

for i in range(fans_count):
    current_sector = input()
    
    if current_sector == 'A':
        sector_a_fans += 1
    elif current_sector == 'B':
        sector_b_fans += 1
    elif current_sector == 'V':
        sector_v_fans += 1
    elif current_sector == 'G':
        sector_g_fans += 1

sector_a_fans = sector_a_fans / fans_count * 100
sector_b_fans = sector_b_fans / fans_count * 100
sector_v_fans = sector_v_fans / fans_count * 100
sector_g_fans = sector_g_fans / fans_count * 100
all_fans = fans_count / stadium_capacity * 100

print(f'{sector_a_fans:.2f}%')
print(f'{sector_b_fans:.2f}%')
print(f'{sector_v_fans:.2f}%')
print(f'{sector_g_fans:.2f}%')
print(f'{all_fans:.2f}%')