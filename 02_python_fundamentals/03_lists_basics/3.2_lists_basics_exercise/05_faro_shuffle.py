deck = input().split(' ')
shuffle_count = int(input())

half = len(deck) // 2

for _ in range(shuffle_count):
    new_deck = []
    first_half = deck[:half]
    second_half = deck[half:]
    
    for i in range(len(first_half)):
        new_deck.append(first_half[i])
        new_deck.append(second_half[i])

    deck = new_deck
    
print(deck)