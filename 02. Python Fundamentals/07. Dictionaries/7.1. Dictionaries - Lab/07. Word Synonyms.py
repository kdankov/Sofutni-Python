from collections import defaultdict

n = int(input())

synonyms = defaultdict(list)

for i in range(n):
    word = input()
    synonym = input()
    
    synonyms[word].append(synonym)

for word in synonyms:
    print(f'{word} - {", ".join(synonyms[word])}')
