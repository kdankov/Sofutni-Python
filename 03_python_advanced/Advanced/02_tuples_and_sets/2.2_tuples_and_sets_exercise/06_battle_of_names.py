names_count = int(input())

even_set = set()
odd_set = set()

for i in range(1, names_count + 1):
    name = input()
    current_sum = 0

    for ch in name:
        current_sum += ord(ch)

    current_sum = int(current_sum / i)

    if current_sum % 2 == 0:
        even_set.add(current_sum)
    else:
        odd_set.add(current_sum)

if sum(even_set) > sum(odd_set):
    symmetric_diff = odd_set ^ even_set

    print(', '.join([str(x) for x in symmetric_diff]))

elif sum(even_set) < sum(odd_set):
    print(', '.join([str(x) for x in odd_set]))

else:
    union = odd_set | even_set

    print(', '.join([str(x) for x in union]))
