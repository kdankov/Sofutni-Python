start_char = ord(input())
end_char = ord(input())

string = input()

total_sum = 0

for ch in string:
    if start_char < ord(ch) < end_char:
        total_sum += ord(ch)

print(total_sum)