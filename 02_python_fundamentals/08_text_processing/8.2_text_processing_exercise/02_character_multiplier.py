strings = input().split()

first_string = [ord(x) for x in strings[0]]
second_string = [ord(x) for x in strings[1]]

total_sum = 0

for i in range(max(len(first_string), len(second_string))):
    if i < len(first_string) and i < len(second_string):
        total_sum += first_string[i] * second_string[i]

    elif i < len(first_string) and i >= len(second_string):      
        total_sum += first_string[i]

    elif i >= len(first_string) and i < len(second_string):
        total_sum += second_string[i]

print(total_sum)