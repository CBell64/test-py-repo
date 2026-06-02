import unittest

# =====================================================================
# ANIMAL CLASSES
# =====================================================================

class Dog:
    def __init__(self, name=None, age=None, breed=None):
        """Overloaded constructor supporting default or parameterized instantiation."""
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self):
        """Overloaded __str__ method to format Dog details."""
        return f"Dog: Name: {self.name}, Age: {self.age}, Breed: {self.breed}"


class Cat:
    def __init__(self, name=None, age=None, fur_color=None):
        """Overloaded constructor supporting default or parameterized instantiation."""
        self.name = name
        self.age = age
        self.fur_color = fur_color

    def __str__(self):
        """Overloaded __str__ method to format Cat details."""
        return f"Cat: Name: {self.name}, Age: {self.age}, Fur Color: {self.fur_color}"


class Bird:
    def __init__(self, name=None, age=None, wingspan=None):
        """Overloaded constructor supporting default or parameterized instantiation."""
        self.name = name
        self.age = age
        self.wingspan = wingspan

    def __str__(self):
        """Overloaded __str__ method to format Bird details."""
        return f"Bird: Name: {self.name}, Age: {self.age}, Wingspan: {self.wingspan}"


# =====================================================================
# KENNEL CLASS
# =====================================================================

class Kennel:
    def __init__(self, animal=None):
        """Overloaded constructor. A kennel can start empty or with one animal."""
        self.animal = animal

    def add_animal(self, animal):
        """Adds an animal if the kennel is currently empty."""
        if self.animal is not None:
            raise ValueError("Cannot add more than one animal to the kennel.")
        self.animal = animal

    def get_animal_type(self):
        """Returns the class name of the animal using the __class__.__name__ attribute."""
        if self.animal is None:
            return "Empty"
        return self.animal.__class__.__name__

    def __str__(self):
        """Overloaded __str__ method matching the required output format."""
        if self.animal is None:
            return "Kennel Animal: Empty"
        return f"Kennel Animal: {str(self.animal)}"


# =====================================================================
# MAIN DRIVER
# =====================================================================

def main():
    print("--- Running Main Driver ---")
    
    # 1. Create animal objects using parameterized constructors
    dog = Dog("Charlie", 7, "Golden Retriever")
    cat = Cat("Luna", 5, "Orange Tabby")
    bird = Bird("Sky", 2, "12 inches")

    # 2. Create Kennel objects and add one animal to each
    kennel1 = Kennel(dog)
    kennel2 = Kennel()  # Starts empty
    kennel2.add_animal(cat)

    # 3. Demonstrate outputs
    print(kennel1)
    print(kennel2)
    
    # 4. Demonstrate "Cannot add more than one animal" constraint
    try:
        print("\nAttempting to add a bird to Charlie's kennel...")
        kennel1.add_animal(bird)
    except ValueError as e:
        print(f"Error caught successfully: {e}")


# =====================================================================
# UNIT TESTS
# =====================================================================

class TestKennelSystem(unittest.TestCase):
    
    def test_animal_str_methods(self):
        dog = Dog("Max", 3, "Labrador")
        cat = Cat("Whiskers", 2, "Black")
        bird = Bird("Pip", 1, "6 inches")
        
        self.assertEqual(str(dog), "Dog: Name: Max, Age: 3, Breed: Labrador")
        self.assertEqual(str(cat), "Cat: Name: Whiskers, Age: 2, Fur Color: Black")
        self.assertEqual(str(bird), "Bird: Name: Pip, Age: 1, Wingspan: 6 inches")

    def test_kennel_get_animal_type(self):
        dog_kennel = Kennel(Dog("Max", 3, "Labrador"))
        empty_kennel = Kennel()
        
        self.assertEqual(dog_kennel.get_animal_type(), "Dog")
        self.assertEqual(empty_kennel.get_animal_type(), "Empty")

    def test_kennel_max_one_animal_constraint(self):
        dog = Dog("Charlie", 7, "Golden Retriever")
        cat = Cat("Luna", 5, "Orange Tabby")
        
        # Test capacity enforcement during initialization vs adding later
        kennel = Kennel(dog)
        with self.assertRaises(ValueError):
            kennel.add_animal(cat)


if __name__ == "__main__":
    # Run the driver code
    main()
    
    print("\n--- Running Unit Tests ---")
    # Run the unit tests (argv=['first-arg-is-ignored'] prevents unittest from looking at system args)
    unittest.main(argv=['first-arg-is-ignored'], exit=False)