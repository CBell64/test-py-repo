from shelter import Shelter, Animal

def main():
    print("--- Animal Shelter Management System ---")
    while True:
        try:
            capacity = int(input("Enter shelter capacity: "))
            if capacity <= 0:
                print("Capacity must be greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")

    shelter = Shelter(capacity)

    while True:
        print("\nShelter Menu:")
        print("1. Add Animal")
        print("2. Remove Animal (Adoption)")
        print("3. Get Animal Information")
        print("4. Process Adoption Requests (if new animals arrive)")
        print("5. View Adopters Waiting List")
        print("6. Exit")
        
        choice = input("Enter your choice (1–6): ").strip()

        if choice == '1':
            name = input("Enter animal name: ").strip()
            species = input("Enter animal species (e.g., Dog, Cat): ").strip()
            try:
                age = int(input("Enter animal age: "))
                animal = Animal(name, species, age)
                print(shelter.add_animal(animal))
            except ValueError:
                print("Invalid age. Animal creation cancelled.")

        elif choice == '2':
            adopter = input("Enter adopter name: ").strip()
            species = input("Enter desired animal species: ").strip()
            print(shelter.adopt_animal(species, adopter))

        elif choice == '3':
            print("\n--- Current Kennels Status ---")
            for info in shelter.get_all_animal_info():
                print(info)

        elif choice == '4':
            print("\nProcessing waiting list updates...")
            results = shelter.process_waiting_list()
            if results:
                for update in results:
                    print(f"[SUCCESS] {update}")
            else:
                print("No pending match updates executed.")

        elif choice == '5':
            print("\n--- Waiting List ---")
            if not shelter.waiting_list or all(len(v) == 0 for v in shelter.waiting_list.values()):
                print("The waiting list is currently empty.")
            else:
                for species, adopters in shelter.waiting_list.items():
                    if adopters:
                        print(f"{species.capitalize()}: {', '.join(adopters)}")

        elif choice == '6':
            print("Exiting Program. Goodbye!")
            break
        else:
            print("Invalid choice! Please select an item from 1 to 6.")

if __name__ == "__main__":
    main()