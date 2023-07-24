def chars_in_range(start, end):
    result = ''
    for i in range(ord(start) + 1, ord(end)):
        result += chr(i) + ' '
    
    return result

start_char = input()
end_char = input()

print(chars_in_range(start_char, end_char))