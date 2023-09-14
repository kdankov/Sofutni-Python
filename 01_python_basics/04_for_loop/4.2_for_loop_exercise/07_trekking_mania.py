groups_count = int(input())

musala = 0
mont_blanc = 0
kilimanjaro = 0
k2 = 0
everest = 0

people_count = 0

for i in range(groups_count):
    people_in_current_group = int(input())
    people_count += people_in_current_group
    
    if people_in_current_group < 6:
        musala += people_in_current_group
    elif people_in_current_group < 13:
        mont_blanc += people_in_current_group
    elif people_in_current_group < 26:
        kilimanjaro += people_in_current_group
    elif people_in_current_group < 41:
        k2 += people_in_current_group
    else:
        everest += people_in_current_group
        
musala = musala / people_count * 100
mont_blanc = mont_blanc / people_count * 100
kilimanjaro = kilimanjaro / people_count * 100
k2 = k2 / people_count * 100
everest = everest / people_count * 100

print(f'{musala:.2f}%')
print(f'{mont_blanc:.2f}%')
print(f'{kilimanjaro:.2f}%')
print(f'{k2:.2f}%')
print(f'{everest:.2f}%')