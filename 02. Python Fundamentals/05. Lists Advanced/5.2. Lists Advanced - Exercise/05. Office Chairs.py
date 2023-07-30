rooms_count = int(input())

total_free_chairs = 0

for i in range(1, rooms_count + 1):
    current_room = input().split()
    free_chairs = len(current_room[0])
    people_count = int(current_room[1])
    
    if people_count > free_chairs:
        print(f'{people_count - free_chairs} more chairs needed in room {i}')
        total_free_chairs -= (people_count - free_chairs)
    else:
        total_free_chairs += free_chairs - people_count
        
if total_free_chairs >= 0:
    print(f'Game On, {total_free_chairs} free chairs left')