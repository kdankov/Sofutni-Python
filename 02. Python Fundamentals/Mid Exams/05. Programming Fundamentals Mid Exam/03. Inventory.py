items = input().split(', ')

command = input()

while command != 'Craft!':
    args = command.split(' - ')
    action = args[0]
    item = args[1]
    
    if action == 'Collect':
        if item not in items:
            items.append(item)
    elif action == 'Drop':
        if item in items:
            items.remove(item)
    elif action == 'Combine Items':
        item_split = item.split(':')
        old_item = item_split[0]
        new_item = item_split[1]
        
        if old_item in items:
            items.insert(items.index(old_item) + 1, new_item)
    elif action == 'Renew':
        if item in items:
            removed_item = items.pop(items.index(item))
            items.append(removed_item)
    
    command = input()
    
print(', '.join(items))