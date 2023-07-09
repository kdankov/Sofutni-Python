one_lev_coins = int(input())
two_leva_coins = int(input())
five_leva_coins = int(input())
sum_to_pay = int(input())

for one in range(one_lev_coins + 1):
    for two in range(two_leva_coins + 1):
        for five in range(five_leva_coins + 1):
            if one * 1 + two * 2 + five * 5 == sum_to_pay:
                print(f'{one} * 1 lv. + {two} * 2 lv. + {five} * 5 lv. = {sum_to_pay} lv.')