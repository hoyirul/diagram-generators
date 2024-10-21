# models/population.py
class Population:
    def __init__(self, species, count):
        self.species = species
        self.count = count

    def display(self):
        return f"{self.species}: {self.count}"

    def increase_population(self, amount):
        self.count += amount

    def decrease_population(self, amount):
        self.count -= amount


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        pass

    def display(self):
        return f"{self.name} is a {self.species}"


class Dog(Animal):
    def make_sound(self):
        return "Bark"

    def fetch(self):
        return "Fetching"


class Cat(Animal):
    def make_sound(self):
        return "Meow"

    def chase_laser(self):
        return "Chasing laser"
