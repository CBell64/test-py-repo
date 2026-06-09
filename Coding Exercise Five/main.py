from models.animal import Dog, Cat
from models.kennel import Kennel

def main():
    print("--- Running Main Driver Demonstration ---\n")

    dog = Dog("Charlie", 7, "Golden Retriever")
    cat = Cat("Luna", 5, "Orange Tabby")

    kennel = Kennel()
    kennel.add_animal(dog)
    print(kennel)

    # This will trigger the capacity error
    kennel.add_animal(cat)

if __name__ == "__main__":
    main()