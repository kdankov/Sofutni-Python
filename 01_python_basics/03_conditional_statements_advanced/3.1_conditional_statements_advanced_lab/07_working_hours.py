hour = int(input())
day = input()

if day == 'Sunday' or 10 > hour or hour > 18:
    print('closed')
else:
    print('open')