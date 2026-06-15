import unittest
from shelter import Shelter, Animal

class TestShelterSystem(unittest.TestCase):

    def setUp(self):
        self.shelter = Shelter(capacity=3)

    def test_add_animal_creates_kennel(self):
        animal = Animal("Buddy", "Dog", 3)
        message = self.shelter.add_animal(animal)
        self.assertEqual(self.shelter.get_total_kennels(), 1)
        self.assertIn("Created Kennel #1", message)

    def test_add_animal_fills_existing_empty_kennel(self):
        dog = Animal("Buddy", "Dog", 3)
        cat = Animal("Whiskers", "Cat", 2)
        
        self.shelter.add_animal(dog)
        self.shelter.adopt_animal("Dog", "Alice") # Frees Kennel #1
        
        message = self.shelter.add_animal(cat)
        self.assertEqual(self.shelter.get_total_kennels(), 1)
        self.assertIn("existing empty Kennel #1", message)

    def test_capacity_limit(self):
        self.shelter.add_animal(Animal("A1", "Dog", 1))
        self.shelter.add_animal(Animal("A2", "Cat", 1))
        self.shelter.add_animal(Animal("A3", "Bird", 1))
        
        # 4th animal should trigger error message
        error_msg = self.shelter.add_animal(Animal("A4", "Dog", 1))
        self.assertIn("maximum capacity", error_msg)
        self.assertEqual(self.shelter.get_total_kennels(), 3)

    def test_waiting_list_placement(self):
        message = self.shelter.adopt_animal("Dragon", "Bob")
        self.assertIn("added to the waiting list", message)
        self.assertIn("Bob", self.shelter.waiting_list["dragon"])