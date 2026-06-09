import unittest
from models.animal import Dog, Cat, Bird
from models.shelter import Shelter

class TestShelterSystem(unittest.TestCase):
    def setUp(self):
        self.shelter = Shelter(capacity=2)
        self.dog = Dog("Charlie", 7, "Golden Retriever")
        self.cat = Cat("Luna", 5, "Orange Tabby")

    def test_add_animal_creates_kennel(self):
        self.shelter.add_animal_to_shelter(self.dog)
        self.assertEqual(len(self.shelter.kennels), 1)

    def test_capacity_limit(self):
        self.shelter.add_animal_to_shelter(self.dog)
        self.shelter.add_animal_to_shelter(self.cat)
        bird = Bird("Pip", 2, "Canary")
        result = self.shelter.add_animal_to_shelter(bird)
        self.assertFalse(result)

    def test_waiting_list_placement(self):
        self.shelter.adopt_animal("Cat", "Bob")
        self.assertIn("Bob", self.shelter.waiting_list["Cat"])