factor = int(input())
count = int(input())

numbers = []

for i in range(1, count + 1):
    numbers.append(i * factor)

print(numbers)