class reverse_iter:
    def __init__(self, iter_obj):
        self.iter_obj = iter_obj
        self.curr_index = len(self.iter_obj) - 1
        self.end_index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr_index <= self.end_index:
            raise StopIteration()

        index = self.curr_index
        self.curr_index -= 1
        return self.iter_obj[index]


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
