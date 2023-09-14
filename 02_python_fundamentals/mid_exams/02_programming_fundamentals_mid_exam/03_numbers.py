numbers = [int(x) for x in input().split()]

average_number = sum(numbers) / len(numbers)

greater_than_average = [num for num in numbers if num > average_number]

if len(greater_than_average) == 0:
    print('No')
else:
    greater_than_average.sort(reverse=True)
    
    if len(greater_than_average) >= 5:
        print(' '.join([str(x) for x in greater_than_average[:5]]))
    else:
        print(' '.join([str(x) for x in greater_than_average]))