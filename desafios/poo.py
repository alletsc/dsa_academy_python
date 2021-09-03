class Dog:
    # atributo da classe
    species = "Canis Familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age


a = Dog('Rex', 13)
b = Dog('pitu', 5)
a == b
