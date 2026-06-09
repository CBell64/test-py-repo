from models.animal import Dog, Cat, Bird
from models.shelter import Shelter

def main():
    # Initialize a shelter capped at 2 total kennels
    shelter = Shelter(capacity=2)

    print("--- 1. Populating Shelter ---")
    dog = Dog("Charlie", 7, "Golden Retriever")
    cat = Cat("Luna", 5, "Orange Tabby")
    bird = Bird("Pip", 2, "Canary")

    shelter.add_animal_to_shelter(dog)  
    shelter.add_animal_to_shelter(cat)  
    shelter.display_status()

    print("--- 2. Testing Capacity Constraint ---")
    shelter.add_animal_to_shelter(bird) 

    print("\n--- 3. Testing Adoption Process ---")
    shelter.adopt_animal("Dog", "Alice")
    shelter.display_status()

    print("--- 4. Re-filling Empty Kennels ---")
    shelter.add_animal_to_shelter(bird)
    shelter.display_status()

    print("--- 5. Testing Waiting List Mechanism ---")
    shelter.adopt_animal("Dog", "Bob")
    shelter.display_status()

if __name__ == "__main__":
    main()