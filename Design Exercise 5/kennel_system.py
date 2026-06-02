import unittest

# =====================================================================
# BASE CLASS (PARENT)
# =====================================================================

class Animal:
    def __init__(self, name=None, age=None):
        """Base class constructor capturing shared attributes."""
        self.name = name
        self.age = age

    def __str__(self):
        """Common string format for all animals."""
        return f"Name: {self.name}, Age: {self.age}"


# =====================================================================
# SUBCLASSES (CHILDREN)
# =====================================================================

class Dog(Animal):
    def __init__(self, name=None, age=None, breed=None):
        """Calls the parent constructor and adds specific attributes."""
        super().__init__(name, age)
        self.breed = breed

    def __str__(self):
        """Leverages parent __str__ and appends unique dog attributes."""
        return f"Dog: {super().__str__()}, Breed: {self.breed}"


class Cat(Animal):
    def __init__(self, name=None, age=None, fur_color=None):
        """Calls the parent constructor and adds specific attributes."""
        super().__init__(name, age)
        self.fur_color = fur_color

    def __str__(self):
        """Leverages parent __str__ and appends unique cat attributes."""
        return f"Cat: {super().__str__()}, Fur Color: {self.fur_color}"


class Bird(Animal):
    def __init__(self, name=None, age=None, wingspan=None):
        """Calls the parent constructor and adds specific attributes."""
        super().__init__(name, age)
        self.wingspan = wingspan

    def __str__(self):
        """Leverages parent __str__ and appends unique bird attributes."""
        return f"Bird: {super().__str__()}, Wingspan: {self.wingspan}"


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
        """Returns the specific class name of the animal using __class__.__name__."""
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
    
    # Create animal objects using parameterized constructors
    dog = Dog("Charlie", 7, "Golden Retriever")
    cat = Cat("Luna", 5, "Orange Tabby")
    bird = Bird("Sky", 2, "12 inches")

    # Create Kennel objects and add one animal to each
    kennel1 = Kennel(dog)
    kennel2 = Kennel()  # Starts empty
    kennel2.add_animal(cat)

    # Output matches requested assignment example format
    print(kennel1)
    print(kennel2)
    
    # Demonstrate "Cannot add more than one animal" constraint safety guard
    try:
        print("\nAttempting to add a bird to Charlie's kennel...")
        kennel1.add_animal(bird)
    except ValueError as e:
        print(f"Error caught successfully: {e}")


# =====================================================================
# UNIT TESTS
# =====================================================================

class TestKennelSystemWithInheritance(unittest.TestCase):
    
    def test_inheritance_relationship(self):
        """Verify that child classes are true instances of the Animal base class."""
        dog = Dog("Max", 3, "Labrador")
        cat = Cat("Whiskers", 2, "Black")
        bird = Bird("Pip", 1, "6 inches")
        
        self.assertTrue(isinstance(dog, Animal))
        self.assertTrue(isinstance(cat, Animal))
        self.assertTrue(isinstance(bird, Animal))

    def test_animal_str_methods(self):
        """Verify that string overrides format correctly using parent class hooks."""
        dog = Dog("Max", 3, "Labrador")
        cat = Cat("Whiskers", 2, "Black")
        
        self.assertEqual(str(dog), "Dog: Name: Max, Age: 3, Breed: Labrador")
        self.assertEqual(str(cat), "Cat: Name: Whiskers, Age: 2, Fur Color: Black")

    def test_kennel_get_animal_type(self):
        """Verify dynamic type extraction via the __name__ layer."""
        dog_kennel = Kennel(Dog("Max", 3, "Labrador"))
        empty_kennel = Kennel()
        
        self.assertEqual(dog_kennel.get_animal_type(), "Dog")
        self.assertEqual(empty_kennel.get_animal_type(), "Empty")

    def test_kennel_max_one_animal_constraint(self):
        """Verify that the kennel rejects subsequent animal additions."""
        kennel = Kennel(Dog("Charlie", 7, "Golden Retriever"))
        with self.assertRaises(ValueError):
            kennel.add_animal(Cat("Luna", 5, "Orange Tabby"))


if __name__ == "__main__":
    # Execute driver logic
    main()
    
    # Execute unit test assertions automatically
    print("\n--- Running Unit Tests ---")
    unittest.main(argv=['first-arg-is-ignored'], exit=False)