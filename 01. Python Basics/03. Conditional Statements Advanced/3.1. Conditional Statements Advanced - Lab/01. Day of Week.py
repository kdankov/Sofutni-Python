day_number = int(input())

days = {
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday',
    7: 'Sunday'
}

if day_number in days:
    print(days[day_number])
else:
    print('Error')