class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def __str__(self):
        return f"Dog: {super().__str__()}, Breed: {self.breed}"

class Cat(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def __str__(self):
        return f"Cat: {super().__str__()}, Fur Color: {self.fur_color}"

class Bird(Animal):
    def __init__(self, name, age, species):
        super().__init__(name, age)
        self.species = species

    def __str__(self):
        return f"Bird: {super().__str__()}, Species: {self.species}"