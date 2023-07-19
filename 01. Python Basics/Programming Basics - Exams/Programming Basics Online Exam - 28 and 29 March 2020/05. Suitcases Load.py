capacity = float(input())

suitcase_volume = input()

loaded_suitcases = 0
no_more_space = False

count = 1

while suitcase_volume != 'End':
    suitcase_volume = float(suitcase_volume)
    
    if count % 3 == 0:
        suitcase_volume *= 1.1
        
    if capacity < suitcase_volume:
        no_more_space = True
        break
    
    capacity -= suitcase_volume
    loaded_suitcases += 1
    
    count += 1
    suitcase_volume = input()
    
if not no_more_space:
    print(f'Congratulations! All suitcases are loaded!')
else:
    print(f'No more space!')

print(f'Statistic: {loaded_suitcases} suitcases loaded.')
