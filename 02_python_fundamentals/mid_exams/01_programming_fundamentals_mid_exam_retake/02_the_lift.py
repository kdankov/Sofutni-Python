waiting_people = int(input())
current_lift_state = [int(x) for x in input().split()]

lift_is_full = False
no_more_people = False

while True:
    for i in range(len(current_lift_state)):
        while current_lift_state[i] < 4:
            if waiting_people == 0:
                no_more_people = True
                break
            current_lift_state[i] += 1
            waiting_people -= 1
    
    if sum(current_lift_state) == 4 * len(current_lift_state):
        lift_is_full = True
        break
    
    if no_more_people:
        break
    
if no_more_people and not lift_is_full:
    print('The lift has empty spots!')
    print(' '.join([str(x) for x in current_lift_state]))
elif waiting_people > 0 and lift_is_full:
    print(f'There isn\'t enough space! {waiting_people} people in a queue!')
    print(' '.join([str(x) for x in current_lift_state]))
else:
    print(' '.join([str(x) for x in current_lift_state]))