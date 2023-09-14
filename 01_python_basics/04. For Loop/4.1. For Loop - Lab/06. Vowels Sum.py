text = input()

vowels_values = {
    'a': 1,
    'e': 2,
    'i': 3,
    'o': 4,
    'u': 5
}

sum = 0

for char in text:
    if char in vowels_values:
        sum += vowels_values[char]
        
print(sum)