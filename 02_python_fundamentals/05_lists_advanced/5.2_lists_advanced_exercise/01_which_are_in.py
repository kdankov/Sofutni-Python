searched_words = input().split(', ')
words = input().split(', ')

final_words = []

for searched_word in searched_words:
    for word in words:
        if searched_word in word and searched_word not in final_words:
            final_words.append(searched_word)
            
print(final_words)