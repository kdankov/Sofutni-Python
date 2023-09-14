numbers = [int(x) for x in input().split()]

even_numbers_iterator = filter(lambda x: x % 2 == 0, numbers)
even_numbers = list(even_numbers_iterator)

print(even_numbers)