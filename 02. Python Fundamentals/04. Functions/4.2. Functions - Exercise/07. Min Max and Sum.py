def min_max_sum(nums):
    nums = [int(x) for x in nums.split()]
        
    return f'The minimum number is {min(nums)} \nThe maximum number is {max(nums)} \nThe sum number is: {sum(nums)}'

numbers = input()

print(min_max_sum(numbers))