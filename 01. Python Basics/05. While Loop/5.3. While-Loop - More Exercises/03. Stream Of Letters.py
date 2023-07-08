letter = input()

c_has_occured = False
o_has_occured = False
n_has_occured = False

current_word = ''
final_word = ''

while letter != 'End':
    append_letter = False
    
    if (letter >= 'a' and letter <= 'z') or (letter >= 'A' and letter <= 'Z'):
        if letter == 'c':
            append_letter = c_has_occured
            c_has_occured = True
        elif letter == 'o':
            append_letter = o_has_occured
            o_has_occured = True
        elif letter == 'n':
            append_letter = n_has_occured
            n_has_occured = True
        else:
            append_letter = True
        
    if append_letter:
        current_word += letter
    
    if o_has_occured and c_has_occured and n_has_occured:
        final_word += current_word + ' '
        current_word = ''
        c_has_occured = False
        o_has_occured = False
        n_has_occured = False
    
    letter = input()
    
print(final_word)