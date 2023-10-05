def age_assignment(*args, **kwargs):
    people = {}

    for name in args:
        people[name] = kwargs[name[0]]

    sorted_people = sorted(people.items(), key=lambda x: x[0])

    result = []
    for name, age in sorted_people:
        result.append(f'{name} is {age} years old.')

    return '\n'.join(result)


print(age_assignment("Peter", "George", G=26, P=19))

print()

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))