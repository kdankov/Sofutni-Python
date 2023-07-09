from math import sqrt, floor

first_pair_start = int(input())
second_pair_start = int(input())

first_pair_end = first_pair_start + int(input())
second_pair_end = second_pair_start + int(input())


for first in range(first_pair_start, first_pair_end + 1):
    for second in range(second_pair_start, second_pair_end + 1):
        is_first_pair_prime = True
        is_second_pair_prime = True
        
        for i in range(2, floor(sqrt(first)) + 1):
            if first % i == 0:
                is_first_pair_prime = False
                break
        
        for i in range(2, floor(sqrt(second)) + 1):
            if second % i == 0:
                is_second_pair_prime = False
                break
        
        if is_first_pair_prime and is_second_pair_prime:
            print(f'{first}{second}')