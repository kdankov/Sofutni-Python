n = int(input())
wanted_word = input()

words = []
special_words = []

for _ in range(n):
    current_input = input()
    
    words.append(current_input)
    
    if wanted_word in current_input:
        special_words.append(current_input)
        
print(words)
print(special_words)
