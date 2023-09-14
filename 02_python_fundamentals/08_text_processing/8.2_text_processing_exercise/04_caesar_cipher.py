text = input()

encrypted_text = ''

for ch in text:
    encrypted_text += chr(ord(ch) + 3)

print(encrypted_text)