first_sequence = set(int(num) for num in input().split())
second_sequence = set(int(num) for num in input().split())
n = int(input())

for _ in range(n):
    command, sequence, *numbers = input().split()

    if command == "Add":
        if sequence == "First":
            [first_sequence.add(int(el)) for el in numbers]
        elif sequence == "Second":
            [second_sequence.add(int(el)) for el in numbers]

    elif command == "Remove":
        if sequence == "First":
            [first_sequence.discard(int(el)) for el in numbers]
        elif sequence == "Second":
            [second_sequence.discard(int(el)) for el in numbers]

    elif command == "Check":
        print(first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence))

print(*sorted(first_sequence), sep=", ")
print(*sorted(second_sequence), sep=", ")
