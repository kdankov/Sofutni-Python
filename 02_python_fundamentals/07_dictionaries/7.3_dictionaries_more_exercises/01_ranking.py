def best_sum(usercontest: dict):
    result = sum([int(x) for x in usercontest.values()])
    return result
 

contests = {}
results = {}

command = input()

best_student = ""
max_points = 0

while command != "end of contests":
    contest, password = command.split(":")
    
    if contest not in contests:
        contests[contest] = password
        
    command = input()
 
command = input()

while command != "end of submissions":
    contest, password, username, points = command.split("=>")
    points = int(points)
 
    if contest in contests and contests[contest] == password:
        if username not in results:
            results[username] = {contest: points}
            
        elif contest in results[username]:
            if points > results[username][contest]:
                results[username][contest] = points
                
        elif contest not in results[username]:
            results[username][contest] = points
            
        if best_sum(results[username]) > max_points:
            max_points = best_sum(results[username])
            best_student = username
            
    command = input()
 
print(f'Best candidate is {best_student} with total {max_points} points.\nRanking:')
for key, value in sorted(results.items()):
    print(f'{key}')
    for course, points in sorted(value.items(), key=lambda x: x[1], reverse=True):
        print(f'#  {course} -> {points}')