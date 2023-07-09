from math import floor

word = input()

vowels = ['a', 'e', 'i', 'o', 'u', 'y']

most_powerful_word = {
    "word": '',
    "points": 0
}

while word != 'End of words':
    current_points = 0
    
    for i in word:
        current_points += ord(i)
    
    if word[0].lower() in vowels:
        current_points *= len(word)
    else:
        current_points = floor(current_points / len(word))
    
    if current_points > most_powerful_word['points']:
        most_powerful_word['word'] = word
        most_powerful_word['points'] = current_points
        
    word = input()
    
print(f'The most powerful word is {most_powerful_word["word"]} - {most_powerful_word["points"]}')
