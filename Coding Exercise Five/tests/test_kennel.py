import unittest
from models.animal import Dog, Cat, Bird
from models.kennel import Kennel

class TestAnimalKennelSystem(unittest.TestCase):
    def test_animal_inheritance(self):
        dog = Dog("Charlie", 7, "Golden Retriever")
        self.assertEqual(dog.name, "Charlie")
        self.assertEqual(dog.breed, "Golden Retriever")

    def test_kennel_adds_one_animal(self):
        kennel = Kennel()
        bird = Bird("Pip", 2, "Canary")
        kennel.add_animal(bird)
        self.assertEqual(kennel.animal, bird)

    def test_kennel_enforces_max_capacity_limit(self):
        kennel = Kennel()
        dog = Dog("Charlie", 7, "Golden Retriever")
        cat = Cat("Luna", 5, "Orange Tabby")

        kennel.add_animal(dog)
        kennel.add_animal(cat) 
        self.assertEqual(kennel.animal, dog)