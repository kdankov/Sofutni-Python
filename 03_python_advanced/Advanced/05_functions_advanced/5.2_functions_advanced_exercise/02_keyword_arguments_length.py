def kwargs_length(**kwargs):
    return len(kwargs)


dictionary_1 = {'name': 'Peter', 'age': 25}
print(kwargs_length(**dictionary_1))

dictionary_2 = {}
print(kwargs_length(**dictionary_2))
