def check_aliquot_sum(num):
    aliquot_sum = 0
    for digit in range(1, num):
        if num % digit == 0:
            aliquot_sum += digit
    
    if num == aliquot_sum:
        return 'We have a perfect number!'
    
    return 'It\'s not so perfect.'


number = int(input())

aliquot_sum = 0

print(check_aliquot_sum(number))
