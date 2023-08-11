text = list(input())

numbers_list = [int(x) for x in text if x.isnumeric()]
non_numbers_list = [x for x in text if not x.isnumeric()]

take_list = numbers_list[::2]
skip_list = numbers_list[1::2]

take_number = 0
skip_number = 0

index = 0
hidden_message = ""

for i in range(len(take_list)):
    take_number = take_list[i]
    skip_number = skip_list[i]
    hidden_message += "".join(non_numbers_list[:take_number])
    del non_numbers_list[0:take_number + skip_number]

print(hidden_message)
