from string import ascii_lowercase, ascii_uppercase
import random

class T3:
    def __init__(self, a):
        self.a = int(a)
            
    
    def run(self):
        chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
        parols = []
        elements = []
        for _ in range(self.a):
            for _ in range(8):
                elements.append(random.choice(chars))
            parols.append("".join(elements))
            elements.clear()
        return " ".join(parols)
