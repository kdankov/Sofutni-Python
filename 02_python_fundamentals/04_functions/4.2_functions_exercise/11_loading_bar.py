def loading_bar(n):
    percentages = ('%' * int(n / 10))
    dots = ('.' * int(10 - n / 10))
    bar = percentages + dots
    return bar

n = int(input())

if n == 100:
    print(f'100% Complete!\n[{loading_bar(n)}]')
else:
    print(f'{n}% [{loading_bar(n)}]\nStill loading...')