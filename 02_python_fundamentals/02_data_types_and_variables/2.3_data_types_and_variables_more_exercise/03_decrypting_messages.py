key = int(input())
n = int(input())

message = ''

for i in range(n):
    current_char = input()
    
    message += chr(ord(current_char) + key)

print(message)
