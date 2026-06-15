import collections

class Animal:
    def __init__(self, name: str, species: str, age: int):
        self.name = name
        self.species = species.strip().lower()
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.species.capitalize()}), Age: {self.age}"


class Kennel:
    def __init__(self, id_num: int):
        self.id_num = id_num
        self.animal = None

    def is_empty(self) -> bool:
        return self.animal is None

    def occupy(self, animal: Animal):
        self.animal = animal

    def vacate(self):
        self.animal = None


class Shelter:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.kennels = []
        self.waiting_list = collections.defaultdict(list)  # species -> list of names

    def get_total_kennels(self) -> int:
        return len(self.kennels)

    def add_animal(self, animal: Animal) -> str:
        # 1. Look for an existing empty kennel first
        for kennel in self.kennels:
            if kennel.is_empty():
                kennel.occupy(animal)
                return f"Placed {animal.name} in existing empty Kennel #{kennel.id_num}."

        # 2. If all kennels are full, try to build a new kennel up to maximum capacity
        if len(self.kennels) < self.capacity:
            new_kennel = Kennel(len(self.kennels) + 1)
            new_kennel.occupy(animal)
            self.kennels.append(new_kennel)
            return f"Created Kennel #{new_kennel.id_num} and placed {animal.name} inside."
        
        return "Error: Shelter is at maximum capacity. Cannot add more kennels or animals."

    def adopt_animal(self, species: str, adopter_name: str) -> str:
        species_lower = species.strip().lower()
        
        # Look for the animal matching the requested species
        for kennel in self.kennels:
            if not kennel.is_empty() and kennel.animal.species == species_lower:
                adopted_animal = kennel.animal
                kennel.vacate()
                return f"Congratulations {adopter_name}! You have adopted {adopted_animal}."

        # Species not found -> add to the waiting list
        self.waiting_list[species_lower].append(adopter_name)
        return f"No {species} available right now. {adopter_name} has been added to the waiting list."

    def process_waiting_list(self) -> list:
        fulfilled_requests = []
        for species_lower, adopters in list(self.waiting_list.items()):
            while adopters:
                # Look for an available animal of this specific species
                found_kennel = None
                for kennel in self.kennels:
                    if not kennel.is_empty() and kennel.animal.species == species_lower:
                        found_kennel = kennel
                        break
                
                if found_kennel:
                    adopter = adopters.pop(0)
                    animal = found_kennel.animal
                    found_kennel.vacate()
                    fulfilled_requests.append(f"{adopter} adopted {animal} from the waiting list.")
                else:
                    break # No more matching animals left right now
                    
        return fulfilled_requests

    def get_all_animal_info(self) -> list:
        info = []
        for kennel in self.kennels:
            status = "Empty" if kennel.is_empty() else str(kennel.animal)
            info.append(f"Kennel #{kennel.id_num}: {status}")
        return info if info else ["The shelter has no kennels yet."]