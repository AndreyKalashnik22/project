class Human:
    def __init__(self, name, surname,age):
        self.name = name
        self.surname = surname
        self.age = age
    species = "Human"
    def think(self):
        print(f"{self.name} is thinking")
    def ASN(self, secondName):
        self.name += secondName
    def info(self):
        print(f"name: {self.name}, surname: {self.surname}, age: {self.age}, species: {self.species}")
    def birthday(self):
        self.age += 1
    def setsurname(self, newSurname):
        self.surname = newSurname
dima = Human("Dima", "Nesterenko", 20)
copybara = Human("Vasya", "Petrovich", 5)
"""print("name: {}, surname: {}, age: {}, speciec: {}".format(dima.name, dima.surname, dima.age, dima.species))
print("name: {}, surname: {}, age: {}, speciec: {}".format(copybara.name, copybara.surname,copybara.age, copybara.species))"""
dima.think()
dima.birthday()
dima.info()
copybara.ASN(" copybaraTurbo")
copybara.setsurname("Sidorovich")
copybara.info()
