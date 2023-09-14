voucher = int(input())

movie_tickets = 0
others = 0

current_input = input()

while current_input != 'End':
    current_price = 0
    
    if len(current_input) > 8:
        current_price = ord(current_input[0]) + ord(current_input[1])
    
        if current_price <= voucher:
            voucher -= current_price
            movie_tickets += 1
        else:
            break
    else:
        current_price = ord(current_input[0])
        
        if current_price <= voucher:
            voucher -= current_price
            others += 1
        else:
            break
        
    current_input = input()
    
print(movie_tickets)
print(others)