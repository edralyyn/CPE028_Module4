import unittest


class Students:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __str__(self):
        return f"{self.name}({self.score})"

s1 = Students("Edralyn", 50)

print(s1.name)
print(s1.score)
print(s1)