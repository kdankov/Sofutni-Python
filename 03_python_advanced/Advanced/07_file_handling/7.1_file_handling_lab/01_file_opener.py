try:
    file = open('text.txt', 'r')
    print('Found')
except FileNotFoundError:
    print('File not found')