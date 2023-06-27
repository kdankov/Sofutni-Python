exam_hour = int(input())
exam_minutes = int(input())
arrive_hour = int(input())
arrive_minutes = int(input())

exam_total_minutes = exam_hour * 60 + exam_minutes
arrive_total_minutes = arrive_hour * 60 + arrive_minutes

if arrive_total_minutes > exam_total_minutes:
    print('Late')
elif exam_total_minutes - arrive_total_minutes <= 30:
    print('On time')
else:
    print('Early')

result = abs(exam_total_minutes - arrive_total_minutes)

if exam_total_minutes - arrive_total_minutes > 0:
    if result < 60:
        print(f'{result} minutes before the start')
    else:
        if result % 60 < 10:
            print(f'{int(result / 60)}:0{result % 60} hours before the start')
        else:
            print(f'{int(result / 60)}:{result % 60} hours before the start')
elif arrive_total_minutes - exam_total_minutes > 0:
    if result < 60:
        print(f'{result} minutes after the start')
    else:
        if result % 60 < 10:
            print(f'{int(result / 60)}:0{result % 60} hours after the start')
        else:
            print(f'{int(result / 60)}:{result % 60} hours after the start')
