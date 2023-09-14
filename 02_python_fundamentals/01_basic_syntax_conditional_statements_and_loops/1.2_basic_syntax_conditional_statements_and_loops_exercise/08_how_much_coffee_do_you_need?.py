event = input()

list_of_events = ['coding', 'dog', 'cat', 'movie']

coffees_count = 0

while event != 'END':
    if event.lower() not in list_of_events:
        event = input()
        continue
    
    if event.islower():
        coffees_count += 1
    else:
        coffees_count += 2
    
    event = input()
    
if coffees_count <= 5:
    print(coffees_count)
else:
    print('You need extra sleep')
