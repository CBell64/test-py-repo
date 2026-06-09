class Kennel:
    def __init__(self):
        self.animal = None

    def add_animal(self, animal):
        if self.animal is None:
            self.animal = animal
        else:
            print("--> Error: The kennel is already occupied. Cannot add another animal.")

    def __str__(self):
        if self.animal is None:
            return "Kennel is empty."
        return f"Kennel Animal: {self.animal}"