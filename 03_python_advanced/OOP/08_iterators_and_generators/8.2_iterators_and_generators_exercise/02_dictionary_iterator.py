class dictionary_iter:
    def __init__(self, dict_obj: dict):
        self.dict_obj = dict_obj
        self.current_index = -1
        self.end_index = len(dict_obj) - 1
        self.items = list(self.dict_obj.items())

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index >= self.end_index:
            raise StopIteration

        self.current_index += 1

        return self.items[self.current_index]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

print()

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
