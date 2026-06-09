from collections import deque
from models.kennel import Kennel

class Shelter:
    def __init__(self, capacity):
        self.capacity = capacity  
        self.kennels = []         
        self.waiting_list = {
            "Dog": deque(),
            "Cat": deque(),
            "Bird": deque()
        }

    def add_animal_to_shelter(self, animal):
        # 1. Try to find an existing empty kennel
        for kennel in self.kennels:
            if kennel.is_empty():
                kennel.add_animal(animal)
                print(f"-> Placed {animal.name} into an existing empty kennel.")
                return True

        # 2. Check capacity before building a new kennel
        if len(self.kennels) < self.capacity:
            new_kennel = Kennel()
            new_kennel.add_animal(animal)
            self.kennels.append(new_kennel)
            print(f"-> Created a new kennel and placed {animal.name} inside.")
            return True

        print(f"--> Error: Cannot add {animal.name}. Shelter capacity reached ({self.capacity} kennels max).")
        return False

    def adopt_animal(self, animal_type, adopter_name):
        target_type = animal_type.strip().capitalize()

        for kennel in self.kennels:
            if not kennel.is_empty() and type(kennel.animal).__name__ == target_type:
                adopted_animal = kennel.remove_animal()
                print(f"🎉 Success! {adopter_name} adopted {adopted_animal.name} ({target_type}).")
                return adopted_animal

        if target_type in self.waiting_list:
            self.waiting_list[target_type].append(adopter_name)
            print(f"⚠️ No {target_type}s available. {adopter_name} added to the waiting list.")
        else:
            print(f"--> Error: {target_type} is not a valid animal type.")
        return None

    def display_status(self):
        print("\n--- Shelter Current Status ---")
        print(f"Kennel Utilization: {len(self.kennels)} / {self.capacity}")
        for i, kennel in enumerate(self.kennels):
            print(f"  Kennel {i+1}: {kennel}")
        print("Waiting Lists:")
        for animal_type, users in self.waiting_list.items():
            print(f"  {animal_type}: {list(users) if users else 'Empty'}")
        print("------------------------------\n")