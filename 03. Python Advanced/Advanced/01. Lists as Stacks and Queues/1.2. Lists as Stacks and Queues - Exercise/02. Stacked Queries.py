n = int(input())

stack = []

for i in range(n):
    query = input()

    if query[0] == '1':
        number = int(query[2:])
        stack.append(number)

    elif query == '2':
        if stack:
            stack.pop()

    elif query == '3':
        if stack:
            print(max(stack))

    elif query == '4':
        if stack:
            print(min(stack))

while len(stack) != 1:
    print(stack.pop(), end=', ')
print(stack.pop())
