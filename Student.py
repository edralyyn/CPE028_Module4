class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}({self.age})"

p1 = Student("Edralyn Peralta", 22)
p2 = Student("Joshua Advincula", 22)

print("My name is", p1.name, "and I am", p1.age, "years old.")
print("Name:", p1.name)
print("Age:", p1.age)
print(p1)

print("My name is", p2.name, "and I am", p2.age, "years old.")
print("Name:", p2.name)
print("Age:", p2.age)
print(p2) 