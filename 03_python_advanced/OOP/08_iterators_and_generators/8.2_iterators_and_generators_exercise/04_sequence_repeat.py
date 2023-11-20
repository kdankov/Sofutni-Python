class sequence_repeat:
    def __init__(self, sequence: str, length: int):
        self.sequence = sequence
        self.length = length
        self.current_index = 0
        self.current_length = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_length >= self.length:
            raise StopIteration

        index = self.current_index
        self.current_index += 1
        self.current_length += 1

        if self.current_index >= len(self.sequence):
            self.current_index = 0

        return self.sequence[index]


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')

print()

result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')
