n = int(input())

numbers = []

for _ in range(n):
    current_number = int(input())
    
    numbers.append(current_number)
    
command = input()

filtered_numbers = []

if command == 'even':
    filtered_numbers = [num for num in numbers if num % 2 == 0]
elif command == 'odd':
    filtered_numbers = [num for num in numbers if num % 2 != 0]
elif command == 'negative':
    filtered_numbers = [num for num in numbers if num < 0]
elif command == 'positive':
    filtered_numbers = [num for num in numbers if num >= 0]

print(filtered_numbers)
