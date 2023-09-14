code = input().split(' | ')

morse_alphabet = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']

result = ''
for word in code:
    args = word.split()
    
    for ch in args:
        current_letter_index = morse_alphabet.index(ch)
        
        current_letter_char = chr(current_letter_index + 97).upper()
        
        result += current_letter_char
    
    result += ' '
    
print(result)