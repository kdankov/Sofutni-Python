numbers = [int(x) for x in input().split(', ')]

for num in numbers:
    if num == 0:
        numbers.append(numbers.pop(numbers.index(num)))

print(numbers)
