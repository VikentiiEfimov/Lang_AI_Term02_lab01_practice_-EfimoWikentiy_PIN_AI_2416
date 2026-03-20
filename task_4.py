class T4:   
    def __init__(self, n):
        self.n = n

    def run(self):
        lst = [str(x) for x in list(BinomialSequence.generate(self.n)) ] 
        return " ".join(lst)

import math
class BinomialSequence:
    def generate(n):
        if n < 0:
            return
        current = 1
        yield current
        for k in range(1, n + 1):
            current = math.factorial(n) // (math.factorial(k) * math.factorial(n-k))
            yield current