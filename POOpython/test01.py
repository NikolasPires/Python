from Person import Person
p1 = Person('Nikolas', 18)
p2 = Person('Jerônimo', 30)
p1.speak('POO')
p2.eat('Ice cream')
p1.eat('Barbecue')
print(p1.currentYear)
print(Person.currentYear)
print(p1.get_birth_year())
print(p2.get_birth_year())