def rounding(numbers):
    numbers = [round(float(x)) for x in numbers.split()]
    
    return numbers

numbers_list = input()

print(rounding(numbers_list))