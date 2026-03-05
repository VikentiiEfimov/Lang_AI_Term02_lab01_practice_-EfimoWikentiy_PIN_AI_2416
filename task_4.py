class T4:   
    def __init__(self, n):
        self.n = n

    def run(self):
        element = []
        for i in range(self.n+1):
            element.append(str(next(BinomialSequence.generate(self.n,i))))
        return " ".join(element)

class BinomialSequence:
    def generate(n,k):
        if n == 0:
            yield 1 
        else:
            yield (next(BinomialSequence.generate(n-1,k)) if k!=n else 0) + (next(BinomialSequence.generate(n-1,k-1)) if k!=0 else 0)