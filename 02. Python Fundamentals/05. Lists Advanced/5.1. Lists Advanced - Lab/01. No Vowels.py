text = list(input())

vowels = ['a', 'o', 'u', 'e', 'i']

print(''.join([x for x in text if x.lower() not in vowels]))
