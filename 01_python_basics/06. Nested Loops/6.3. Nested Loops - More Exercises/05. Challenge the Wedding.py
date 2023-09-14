men = int(input())
women = int(input())
tables = int(input())

out_of_tables = False

for i in range(1, men + 1):
    for j in range(1, women + 1):
        print(f'({i} <-> {j})', end=' ')
        
        tables -= 1
        if tables == 0:
            out_of_tables = True
            break
        
    if out_of_tables:
        break