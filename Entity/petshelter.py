class PetShelter:
    def __init__(self):
        self.available_pets = []

    def add_pet(self, pet):
        self.available_pets.append(pet)
        print(f"Pet {pet} added to the shelter.")

    def remove_pet(self, pet):
        if pet in self.available_pets:
            self.available_pets.remove(pet)
            print(f"Pet {pet} removed from the shelter.")
        else:
            print(f"Pet {pet} not found in the shelter.")

    def list_available_pets(self):
        print("Available pets in the shelter:")
        for pet in self.available_pets:
            print(pet)

