def absolute_values(nums):
    absolute = [abs(float(x)) for x in nums.split()]
    
    return absolute

numbers = input()

print(absolute_values(numbers))