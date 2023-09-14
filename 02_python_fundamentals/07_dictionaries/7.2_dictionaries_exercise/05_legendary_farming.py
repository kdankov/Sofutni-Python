key_materials = {
    'shards': 0,
    'fragments': 0,
    'motes': 0
}

junk = {}

obtained_item = None

while obtained_item == None:
    materials = input().split()
    
    for i in range(0, len(materials), 2):
        quantity = int(materials[i])
        material = materials[i + 1].lower()
        
        if material in key_materials.keys():
                key_materials[material] += quantity
        else:
            if material not in junk:
                junk[material] = 0
            junk[material] += quantity

        for key, value in key_materials.items():
            if value < 250:
                continue
            
            key_materials[key] -= 250
            
            if key == 'shards':
                obtained_item = 'Shadowmourne'
                break
            elif key == 'fragments':
                obtained_item = 'Valanyr'
                break
            elif key == 'motes':
                obtained_item = 'Dragonwrath'
                break
            
        if obtained_item is not None:
            break
            
print(f'{obtained_item} obtained!')

[print(f'{key}: {value}') for key, value in key_materials.items()]
[print(f'{key}: {value}') for key, value in junk.items()]
