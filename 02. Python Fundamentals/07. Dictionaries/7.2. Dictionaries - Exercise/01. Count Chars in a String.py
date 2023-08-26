from collections import defaultdict

word = input()

dictionary = defaultdict(int)

for letter in word:
    if letter != ' ':
        dictionary[letter] += 1

[print(f'{letter} -> {occurances}') for letter, occurances in dictionary.items()]