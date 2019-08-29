class Animal():
    def __init__(self, species, noise):
        self.species = species
        self.noise = noise
    def sound(self):
        print(self.noise)
    def get_species(self):
        return self.species

class Cat(Animal):
    def __init__(self):
        super().__init__("cat", "meow")
    def meow(self):
        self.sound()

d = Animal("Dog", "Woof")
d.sound()

c = Animal("Cat", "meow")
c.sound()
c = Cat()
c.sound()
c.meow()