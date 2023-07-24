number_list = input().split(", ")
resultArr = list(map(lambda x: 'True' if (x == x[::-1]) else 'False', number_list))
print('\n'.join(resultArr))