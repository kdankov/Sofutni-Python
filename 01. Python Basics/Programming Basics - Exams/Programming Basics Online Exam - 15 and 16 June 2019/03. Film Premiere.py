movie = input()
package = input()
tickets_count = int(input())

bill = 0

if movie == 'John Wick':
    if package == 'Drink':
        bill = 12 * tickets_count
    elif package == 'Popcorn':
        bill = 15 * tickets_count
    elif package == 'Menu':
        bill = 19 * tickets_count
elif movie == 'Star Wars':
    if package == 'Drink':
        bill = 18 * tickets_count
    elif package == 'Popcorn':
        bill = 25 * tickets_count
    elif package == 'Menu':
        bill = 30 * tickets_count
    
    if tickets_count >= 4:
        bill *= 0.7
elif movie == 'Jumanji':
    if package == 'Drink':
        bill = 9 * tickets_count
    elif package == 'Popcorn':
        bill = 11 * tickets_count
    elif package == 'Menu':
        bill = 14 * tickets_count
        
    if tickets_count == 2:
        bill *= 0.85
        
print(f'Your bill is {bill:.2f} leva.')