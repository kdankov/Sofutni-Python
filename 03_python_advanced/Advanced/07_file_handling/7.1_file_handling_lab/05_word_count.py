import re

with open('words.txt', 'r') as file:
    searched_words = file.read().split()

with open('input.txt', 'r') as file:
    text = file.read().lower()

words = {}

for word in searched_words:
    pattern = re.compile(rf'\b{word}\b')
    result = re.findall(pattern, text)
    words[word] = len(result)

with open('output.txt', 'w') as file:
    for key, value in sorted(words.items(), key=lambda x: -x[1]):
        file.write(f'{key} - {value}\n')