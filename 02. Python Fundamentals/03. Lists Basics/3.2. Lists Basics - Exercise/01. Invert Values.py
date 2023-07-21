numbers = input().split(' ')


numbers_list = [int(num) for num in numbers]
numbers_list = [num * -1 for num in numbers_list]

print(numbers_list)