class T2:
    def __init__(self, my_tuple):
        self.my_tuple = my_tuple
    
    def run(self):
        try:
            iterator = CyclicTupleIterator(self.my_tuple)
            elements = []
            for _ in range(int(len(self.my_tuple)*2.71828)):
                elements.append(str(next(iterator)))
            return " ".join(elements)
        except StopIteration:
            return "Пустой кортеж: итерация остановлена (StopIteration)"

class CyclicTupleIterator:
    def __init__(self, data: tuple):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if not self.data:
            raise StopIteration
        value = self.data[self.index]
        self.index = (self.index + 1) % len(self.data)
        return value