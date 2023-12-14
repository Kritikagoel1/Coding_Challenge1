class AdoptionException(Exception):
    def __init__(self, message="Adoption error occurred."):
        self.message = message
        super().__init__(self.message)

class Pet:
    def __init__(self, name, available=True):
        self.Name = name
        self.Available = available

class AdoptionPlatform:
    def __init__(self):
        self.available_pets = [Pet("Buddy"), Pet("Whiskers"), Pet("Max")]

    def adopt_pet(self, pet_name):
        try:
            pet = self.find_pet_by_name(pet_name)
            if pet is not None and pet.Available:
                # Process adoption logic (not implemented in this example)
                print(f"Adopted {pet.Name} successfully!")
                pet.Available = False
            elif pet is not None and not pet.Available:
                raise AdoptionException(f"{pet.Name} is already adopted.")
            else:
                raise AdoptionException(f"No pet found with the name {pet_name}.")
        except AdoptionException as e:
            print(f"Adoption failed: {e}")

    def find_pet_by_name(self, pet_name):
        for pet in self.available_pets:
            if pet.Name == pet_name:
                return pet
        return None


platform = AdoptionPlatform()

try:

    pet_to_adopt = input("Enter the name of the pet you want to adopt: ")
    platform.adopt_pet(pet_to_adopt)
except ValueError:
    print("Error: Please enter a valid input.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
