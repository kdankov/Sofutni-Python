last_sector = input()
starting_rows = int(input())
odd_row_seats = int(input())

ODD_ROW_SEATS = odd_row_seats

all_seats_count = 0

for i in range(ord('A'), ord(last_sector) + 1):
    current_row = 1 
    for j in range(1, starting_rows + 1):
        if current_row % 2 == 0:
            odd_row_seats += 2
        else:
            odd_row_seats = ODD_ROW_SEATS
        
        current_seat = ord('a')
        for k in range(1, odd_row_seats + 1):
            print(f'{chr(i)}{j}{chr(current_seat)}')
            current_seat += 1
            all_seats_count += 1
        
        current_row += 1
            
    starting_rows += 1
    
print(all_seats_count)