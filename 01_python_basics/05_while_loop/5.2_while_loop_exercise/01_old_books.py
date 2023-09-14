wanted_book = input()

count = 0
book_found = False

current_book = input()

while current_book != 'No More Books':
    if current_book == wanted_book:
        book_found = True
        print(f'You checked {count} books and found it.')
        break
        
    count += 1
    current_book = input()
    
if not book_found:
    print('The book you search is not here!')
    print(f'You checked {count} books.')