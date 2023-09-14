brackets = input()

stack = []

is_balanced = True

if len(brackets) % 2 != 0:
    print('NO')
else:
    for bracket in brackets:
        if bracket == '{' or bracket == '[' or bracket == '(':
            stack.append(bracket)
        else:
            if bracket == '}':
                if stack[-1] == '{':
                    stack.pop()
            elif bracket == ']':
                if stack[-1] == '[':
                    stack.pop()
            elif bracket == ')':
                if stack[-1] == '(':
                    stack.pop()

    if len(stack) > 0:
        print('NO')
    else:
        print('YES')
