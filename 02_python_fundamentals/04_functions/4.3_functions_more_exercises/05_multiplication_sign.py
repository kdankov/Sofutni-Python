def check_multiplication(num1, num2, num3):
    count = 0
    is_zero = False
    numbers_list = [num1, num2, num3]
    
    for i in range(len(numbers_list)):
        if num1 == 0 or num2 == 0 or num3 == 0:
            is_zero = True
            break
        elif numbers_list[i] < 0:
            count += 1
            
    if count == 1 or count == 3:
        return 'negative'
    elif is_zero:
        return 'zero'
    else:
        return 'positive'

first_num = int(input())
second_num = int(input())
third_num = int(input())

print(check_multiplication(first_num, second_num, third_num))

