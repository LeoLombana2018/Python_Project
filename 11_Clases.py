### Class ###

class Person:
   
    def __init__ (self, name, surname, alias = "Sin alias"):
        self.fullname = f"{name} {surname} {alias}"

    def walk (self):
        print(f"{self.fullname} esta caminando")

my_person = Person("Leonardo", "Lombana")
print(my_person.fullname)
my_person.walk()

my_other_person = Person("Leonardo", "Lombana", "calb-eagle")
print(my_other_person.fullname)
my_other_person.walk()