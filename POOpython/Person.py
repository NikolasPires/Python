from datetime import datetime
class Person:
    currentYear = int(datetime.strftime(datetime.now(), '%Y'))
    def __init__(self, name, age, eating=False, speaking=False):
        self.name = name
        self.age = age
        self.eating = eating
        self.speaking = speaking


    def speak(self, content):
        if self.eating:
            print(f'{self.name} can not speak while eat')
            return

        if self.speaking:
            print(f'{self.name} is already speaking.')
            return

        print(f'{self.name} is speaking about {content}.')
        self.speaking = True

    def quiet(self):
        if not self.speaking:
            print(f'{self.name} is already quiet')
            return

        print(f'{self.name} stayed quiet.')
        self.speaking = False


    def eat(self, food):
        if self.eating:
            print(f'{self.name} is still eating.')
            return

        if self.speaking:
            print(f'{self.name} can not eat while speak.')
            return

        print(f'{self.name} is eating {food}.')
        self.eating = True


    def stop_eat(self):
        if not self.eating:
            print(f'{self.name} is not eating.')
            return

        print(f'{self.name} stop to eating.')
        self.eating = False

    def get_birth_year(self):
        return self.currentYear - self.age
