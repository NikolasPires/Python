from random import randint

class Person:
    current_year = 2021
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def get_birth_year(self):
        print(self.current_year - self.age)

    @classmethod
    def by_birth_year(cls, name, birth_year):
        age = cls.current_year - birth_year
        return cls(name, age)


    @staticmethod
    def id():
        rand = randint(10000, 19999)
        return rand


p1 = Person.by_birth_year('Nikolas', 2003)
print(p1)
print(p1.age, p1.name)
print(Person.id())
print((p1.id()))