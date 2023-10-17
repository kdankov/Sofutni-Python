from collections import deque

seats = input().split(', ')
first_sequence = deque([int(x) for x in input().split(', ')])
second_sequence = deque([int(x) for x in input().split(', ')])

rotations_count = 0
seat_matches = []

while True:
    if len(seat_matches) == 3 or rotations_count == 10:
        break

    current_num_first_seq = first_sequence.popleft()
    current_num_second_seq = second_sequence.pop()
    ascii_value = chr(current_num_first_seq + current_num_second_seq)

    first_match = str(current_num_first_seq) + str(ascii_value)
    second_match = str(current_num_second_seq) + str(ascii_value)

    for seat in [first_match, second_match]:
        if seat in seat_matches:
            break
        if seat in seats:
            seat_matches.append(seat)
            break
    else:
        first_sequence.append(current_num_first_seq)
        second_sequence.appendleft(current_num_second_seq)

    rotations_count += 1

print(f'Seat matches: {", ".join(seat_matches)}')
print(f'Rotations count: {rotations_count}')