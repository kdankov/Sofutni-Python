from functools import reduce


def operate(sign, *args):
    # if sign == '+':
    #     return reduce(lambda a, b: a + b, args)
    # elif sign == '-':
    #     return reduce(lambda a, b: a - b, args)
    # elif sign == '*':
    #     return reduce(lambda a, b: a * b, args)
    # elif sign == '/':
    #     return reduce(lambda a, b: a / b, args)

    return reduce(lambda a, b: eval(f'{a}{sign}{b}'), args)


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))