initial_string = input()

indexes_list = []

for index, value in enumerate(initial_string):
    if value.isupper():
        indexes_list.append(index)
    
print(indexes_list)