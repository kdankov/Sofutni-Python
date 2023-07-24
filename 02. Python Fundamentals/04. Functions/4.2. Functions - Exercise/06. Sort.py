def sorted_numbers(nums):
    nums = [int(x) for x in nums]
    
    return(sorted(nums))
    
numbers = input().split()

print(sorted_numbers(numbers))