from string import ascii_lowercase, ascii_uppercase
import random

class T3:   
    def run(self):
        parols = []
        gen = self.password_generator()
        for i in range(5):
            parols.append(f"{i+1}: {next(gen)}")
        return " ".join(parols)

    def password_generator(self):
        chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
        while True:
            password = ''.join(random.choice(chars) for _ in range(8))
            yield password
