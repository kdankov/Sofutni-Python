word = input()

while word != 'End':
    if word == 'SoftUni':
        word = input()
        continue
    
    for i in word:
        print(i * 2, end='')
        
    print()
        
    word = input()
