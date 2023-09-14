snowballs_count = int(input())

best_snowball = {
    'weight': 0,
    'time': 0,
    'value': 0,
    'quality': 0
}

for i in range(snowballs_count):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    
    snowball_value = int((snowball_weight / snowball_time) ** snowball_quality)

    if snowball_value > best_snowball['value']:
        best_snowball['weight'] = snowball_weight
        best_snowball['time'] = snowball_time
        best_snowball['value'] = snowball_value
        best_snowball['quality'] = snowball_quality
        
print(f'{best_snowball["weight"]} : {best_snowball["time"]} = {best_snowball["value"]} ({best_snowball["quality"]})')
