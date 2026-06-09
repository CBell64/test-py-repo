class Kennel:
    def __init__(self):
        self.animal = None

    def is_empty(self):
        return self.animal is None

    def add_animal(self, animal):
        if self.is_empty():
            self.animal = animal
            return True
        return False

    def remove_animal(self):
        removed = self.animal
        self.animal = None
        return removed

    def __str__(self):
        if self.is_empty():
            return "Empty Kennel"
        return f"Kennel containing [{self.animal}]"