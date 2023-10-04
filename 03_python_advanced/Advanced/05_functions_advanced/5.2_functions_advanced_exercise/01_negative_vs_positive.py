def numbers_sums(*args):
    neg_sum = 0
    pos_sum = 0

    for num in args:
        if num > 0:
            pos_sum += num
        elif num < 0:
            neg_sum += num

    return neg_sum, pos_sum


nums = [int(x) for x in input().split()]

print(numbers_sums(*nums)[0])
print(numbers_sums(*nums)[1])

if abs(numbers_sums(*nums)[0]) > numbers_sums(*nums)[1]:
    print('The negatives are stronger than the positives')
elif abs(numbers_sums(*nums)[0]) < numbers_sums(*nums)[1]:
    print('The positives are stronger than the negatives')