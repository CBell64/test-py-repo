class Dog:
    def __init__(self, name="Unknown", age=0, breed="Mixed"):
        """Overloaded constructor using default arguments."""
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self):
        return f"Dog [Name: {self.name}, Age: {self.age}, Breed: {self.breed}]"


class Cat:
    def __init__(self, name="Unknown", age=0, fur_color="Short Hair"):
        """Overloaded constructor using default arguments."""
        self.name = name
        self.age = age
        self.fur_color = fur_color

    def __str__(self):
        return (
            f"Cat [Name: {self.name}, Age: {self.age}, Fur: {self.fur_color}]"
        )


class Bird:
    def __init__(self, name="Unknown", age=0, wingspan=0.0):
        """Overloaded constructor using default arguments."""
        self.name = name
        self.age = age
        self.wingspan = wingspan

    def __str__(self):
        return f"Bird [Name: {self.name}, Age: {self.age}, Wingspan: {self.wingspan}cm]"


class Kennel:
    def __init__(self, animal=None):
        """Overloaded constructor accepting any animal object."""
        self.animal = animal

    def get_animal_type(self):
        """Returns the class name string of the contained animal."""
        if self.animal:
            return type(self.animal).__name__
        return "Empty Kennel"

    def __str__(self):
        if self.animal:
            return f"Kennel containing a {self.get_animal_type()}: {str(self.animal)}"
        return "This kennel is currently empty."


# --- Demonstration of Containment ---
if __name__ == "__main__":
    # Instantiate different animal objects
    buddy = Dog("Buddy", 3, "Golden Retriever")
    whiskers = Cat("Whiskers", 2, "Calico")
    pip = Bird("Pip", 1, 12.5)

    # Put Dog into Kennel
    kennel_1 = Kennel(buddy)
    print(kennel_1)
    print(f"Type checked: {kennel_1.get_animal_type()}\n")

    # Put Cat into Kennel
    kennel_2 = Kennel(whiskers)
    print(kennel_2)
    print(f"Type checked: {kennel_2.get_animal_type()}\n")

    # Put Bird into Kennel
    kennel_3 = Kennel(pip)
    print(kennel_3)
    print(f"Type checked: {kennel_3.get_animal_type()}\n")