wanted_height = int(input())

starting_height = wanted_height - 30
jumps_count = 0
    
has_failed = False

while starting_height <= wanted_height:
    for i in range(3):
        jumps_count += 1
        current_jump = int(input())
            
        if current_jump > starting_height:
            starting_height += 5
            break;
        if i == 2:
            print(f'Tihomir failed at {starting_height}cm after {jumps_count} jumps.')
            has_failed = True
            break
        
        if has_failed:
            break
    if has_failed:
        break

if not has_failed:
    print(f'Tihomir succeeded, he jumped over {wanted_height}cm after {jumps_count} jumps.')

