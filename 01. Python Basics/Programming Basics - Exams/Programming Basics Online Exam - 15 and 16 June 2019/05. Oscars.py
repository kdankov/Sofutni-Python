actor = input()
academy_points = float(input())
judges_count = int(input())

got_nominee = False

points = academy_points

for i in range(judges_count):
    current_judge = input()
    current_points = float(input())
    
    points += len(current_judge) * current_points / 2
    
    if points >= 1250.5:
        got_nominee = True
        break
    
if got_nominee:
    print(f'Congratulations, {actor} got a nominee for leading role with {points:.1f}!')
else:
    print(f'Sorry, {actor} you need {1250.5 - points:.1f} more!')