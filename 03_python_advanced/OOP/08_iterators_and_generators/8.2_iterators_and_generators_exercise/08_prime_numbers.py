from collections import deque
from math import sqrt


def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def get_primes(numbers: list):
    numbers = deque(numbers)
    while numbers:
        current_number = numbers.popleft()
        if is_prime(current_number):
            yield current_number


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print(list(get_primes([-2, 0, 0, 1, 1, 0])))