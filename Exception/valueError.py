class PetShelter:
    def __init__(self):
        self.availablePets = []

    def add_pet(self, pet):
        self.availablePets.append(pet)

    def remove_pet(self, pet):
        if pet in self.availablePets:
            self.availablePets.remove(pet)

    def list_available_pets(self):
        for pet in self.availablePets:
            try:
                print(f"Pet: {pet.Name}, Age: {pet.Age}, Breed: {pet.Breed}")
            except AttributeError as e:
                print(f"Error accessing pet information: {e}. Information might be missing.")


shelter = PetShelter()

try:

    pet_name = input("Enter pet name: ")
    pet_age = int(input("Enter pet age: "))
    pet_breed = input("Enter pet breed: ")


    new_pet = Pet(pet_name, pet_age, pet_breed)
    shelter.add_pet(new_pet)

    print(f"Pet {new_pet.Name} added to the shelter.")
except ValueError:
    print("Error: Please enter a valid integer for pet age.")


print("\nList of available pets:")
shelter.list_available_pets()
