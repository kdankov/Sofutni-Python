from collections import defaultdict

words = input().split()

dictionary = defaultdict(int)

for word in words:
    word_lower = word.lower()
    
    dictionary[word_lower] += 1
    
for (key, value) in dictionary.items():
    if value % 2 != 0:
        print(key, end=' ')
