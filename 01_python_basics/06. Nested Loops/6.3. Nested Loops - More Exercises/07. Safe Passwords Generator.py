# SOLUTION 1
# ---------------------------------------
a = int(input())
b = int(input())
max_count = int(input())
current_count = 0
symbol_A = 35
symbol_B = 64
 
for x in range(1,  + 1):
    for y in range(1, b + 1):
        current_count += 1
        if current_count > max_count:
            break
        if symbol_A > 55:
            symbol_A = 35
        if symbol_B > 96:
            symbol_B = 64
        print(f"{chr(symbol_A)}{chr(symbol_B)}{x}{y}{chr(symbol_B)}{chr(symbol_A)}", end="|")
        symbol_A += 1
        symbol_B += 1
        
# SOLUTION 2
# ---------------------------------------      
# a = int(input())
# b = int(input())
# max_count = int(input())

# current_count = 0

# flag = False

# for A in range(35, 55):
#     for B in range(64, 96):
#         for x in range(1, a + 1):
#             for y in range(1, b + 1):
#                 current_count += 1 
                
#                 if current_count > max_count:
#                     flag = True
#                     break
#                 print(f'{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}', end='|')
                
#                 if x == a and y == b:
#                     flag = True
#                     break
                
#                 A += 1
#                 if A > 55:
#                     A = 35
                
#                 B += 1
#                 if B > 96:
#                     B = 64
            
#             if flag:
#                 break
#         if flag:
#             break
#     if flag:
#         break
    