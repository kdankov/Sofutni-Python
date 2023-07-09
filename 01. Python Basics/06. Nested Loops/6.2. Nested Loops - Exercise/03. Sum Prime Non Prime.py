num = input()

prime_sum = 0
non_prime_sum = 0

is_prime = False

while num != 'stop':
    num = int(num)
    
    if num < 0:
        print('Number is negative.')
        num = input()
        continue
	
    is_prime = True
    
    if num == 1:
        is_prime = False
    else:
        for i in range(num, 1, -1):
            if num % i == 0 and i != num:
                is_prime = False
                break
            
    if is_prime:
        prime_sum += num
    else:
        non_prime_sum += num
        
    num = input()
    
print(f'Sum of all prime numbers is: {prime_sum}')
print(f'Sum of all non prime numbers is: {non_prime_sum}')