initial_string = input()
target_string = input()

final_string = ''

for i in range(1, len(initial_string) + 1):
    final_string = target_string[:i] + initial_string[i:]
    
    if initial_string[i - 1] != target_string[i - 1]:
        print(final_string)
    
