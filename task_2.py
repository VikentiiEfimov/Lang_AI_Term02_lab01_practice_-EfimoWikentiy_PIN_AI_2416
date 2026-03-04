class T2:
    def __init__(self, my_tuple):
        self.my_tuple = my_tuple
    
    def run(self):
        iterator = CyclicTupleIterator(self.my_tuple)
        elements = []
        for _ in range(len(self.my_tuple)):
            elements.append(str(next(iterator)))
        return " ".join(elements)


class CyclicTupleIterator:
    def __init__(self, data: tuple):
        self.data = data
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        return self.data[self.index]