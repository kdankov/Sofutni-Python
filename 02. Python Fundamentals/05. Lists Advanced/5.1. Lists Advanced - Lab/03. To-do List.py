notes = {}

command = input()
while command != "End":
    tokens = command.split("-")
    importance = int(tokens[0])
    value = tokens[1]
    notes[importance] = value
    command = input()

result = []

for task in sorted(notes.items()):
    result.append(task[1])

print(result)