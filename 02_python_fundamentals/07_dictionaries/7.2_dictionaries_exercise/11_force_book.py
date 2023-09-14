current_line = input()

force_book = {}

while current_line != "Lumpawaroo":
    if "|" in current_line:
        args = current_line.split(" | ")
        side = args[0]
        user = args[1]

        check = False
        
        for key, value in force_book.items():
            if user in value:
                check = True
                break
            
        if not check:
            if side not in force_book:
                force_book[side] = [user]
                
            elif side in force_book and user not in force_book[side]:
                force_book[side].append(user)
                
    elif "->" in current_line:
        args = current_line.split(" -> ")
        user = args[0]
        side = args[1]
        
        for key, value in force_book.items():
            if user in value:
                value.remove(user)
                break

        if side not in force_book:
            force_book[side] = [user]
            print(f"{user} joins the {side} side!")
            
        elif side in force_book and user not in force_book[side]:
            force_book[side].append(user)
            print(f"{user} joins the {side} side!")
            
    current_line = input()
    
for key, value in force_book.items():
    if len(value) > 0:
        print(f"Side: {key}, Members: {len(value)}")
        
        for v in value:
            print(f"! {v}")